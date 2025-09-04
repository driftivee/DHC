import os
import asyncio
import aiohttp
import time

# =====================
# সুন্দর Banner Function
# =====================
def banner():
    os.system("clear")
    print("="*60)
    print("     🚀 Driftivee Load Testing Tool 🚀")
    print("="*60)
    print(r"""
     ██████╗ ██████╗ ██╗███████╗████████╗██╗██╗   ██╗███████╗███████╗
    ██╔════╝██╔═══██╗██║██╔════╝╚══██╔══╝██║██║   ██║██╔════╝██╔════╝
    ██║     ██║   ██║██║███████╗   ██║   ██║██║   ██║█████╗  ███████╗
    ██║     ██║   ██║██║╚════██║   ██║   ██║╚██╗ ██╔╝██╔══╝  ╚════██║
    ╚██████╗╚██████╔╝██║███████║   ██║   ██║ ╚████╔╝ ███████╗███████║
     ╚═════╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝  ╚══════╝╚══════╝
    """)
    print("                Created by: Driftivee ❤️\n")
    print(" [1] Owner Contact")
    print(" [2] Load Tester")
    print(" [0] Exit")
    print("="*60)

# =====================
# Load Testing Function
# =====================
async def fetch(session, url):
    try:
        async with session.get(url) as response:
            await response.text()
            return response.status
    except Exception:
        return None

async def run_load_test(url, num_requests, concurrency):
    tasks = []
    connector = aiohttp.TCPConnector(limit=concurrency)
    async with aiohttp.ClientSession(connector=connector) as session:
        start_time = time.time()
        for _ in range(num_requests):
            tasks.append(fetch(session, url))
        results = await asyncio.gather(*tasks)
        end_time = time.time()

    success = sum(1 for r in results if r == 200)
    fail = sum(1 for r in results if r is None)
    print(f"\n✅ Completed in {end_time - start_time:.2f} seconds")
    print(f"✔️ Success: {success}")
    print(f"❌ Failed: {fail}\n")

# =====================
# Main Menu
# =====================
def main():
    while True:
        banner()
        choice = input("Select an option: ")
        if choice == "1":
            print("\n📧 Contact: driftivepqy@gmail.com\n")
            input("Press Enter to go back...")
        elif choice == "2":
            url = input("\n🌐 Enter target URL: ")
            num_requests = int(input("🔁 Number of requests: "))
            concurrency = int(input("⚡ Concurrency: "))
            asyncio.run(run_load_test(url, num_requests, concurrency))
            input("Press Enter to go back...")
        elif choice == "0":
            print("\n👋 Exiting... Goodbye!\n")
            break
        else:
            print("\n❌ Invalid option! Try again.\n")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
