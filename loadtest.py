import argparse
import asyncio
import aiohttp
import time

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            await response.text()
            return response.status
    except Exception as e:
        return f"Error: {e}"

async def worker(name, url, requests, results):
    async with aiohttp.ClientSession() as session:
        for _ in range(requests):
            status = await fetch(session, url)
            results.append(status)

async def run_load_test(url, total_requests, concurrency):
    tasks = []
    results = []
    requests_per_worker = total_requests // concurrency

    start_time = time.time()

    for i in range(concurrency):
        task = asyncio.create_task(worker(i, url, requests_per_worker, results))
        tasks.append(task)

    await asyncio.gather(*tasks)

    end_time = time.time()
    duration = end_time - start_time

    # Stats
    success = results.count(200)
    errors = len(results) - success

    print("\n📊 Load Test Result")
    print(f"Total Requests: {total_requests}")
    print(f"Concurrency: {concurrency}")
    print(f"Time Taken: {duration:.2f} sec")
    print(f"Successful (200): {success}")
    print(f"Errors/Other: {errors}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple HTTP Load Testing Tool (Termux Compatible)")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("-n", "--requests", type=int, default=100, help="Total number of requests")
    parser.add_argument("-c", "--concurrency", type=int, default=10, help="Number of concurrent workers")

    args = parser.parse_args()

    asyncio.run(run_load_test(args.url, args.requests, args.concurrency))
