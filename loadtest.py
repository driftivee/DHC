import os
import asyncio
import aiohttp
import time
import pyfiglet
from termcolor import colored

# =====================
# Banner Function
# =====================
def banner():
    os.system("clear")
    ascii_banner = pyfiglet.figlet_format("Driftivee Tool")
    print(colored(ascii_banner, "cyan"))
    print(colored("                Created by: Driftivee ❤️", "yellow"))
    print("=" * 60)
    print(" [1] Owner Contact")
    print(" [2] Load Tester")
    print(" [0] Exit")
    print("=" * 60)

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

    print(colored(f"\n✅ Completed in {end_time - start_time:.2f} seconds", "cyan"))
    print(colored(f"✔️ Success: {success}", "green"))
    print(colored(f"❌ Failed: {fail}\n", "red"))

# =====================
# Main Menu
# =====================
def main():
    while True:
        banner()
        choice = input("Select an option: ")
        if choice == "1":
            print(colored("\n📧 Contact: driftivepqy@gmail.com\n", "yellow"))
            input("Press Enter to go back...")
        elif choice == "2":
            url = input("\n🌐 Enter target URL: ")
            num_requests = int(input("🔁 Number of requests: "))
            concurrency = int(input("⚡ Concurrency: "))
            asyncio.run(run_load_test(url, num_requests, concurrency))
            input("Press Enter to go back...")
        elif choice == "0":
            print(colored("\n👋 Exiting... Goodbye!\n", "magenta"))
            break
        else:
            print(colored("\n❌ Invalid option! Try again.\n", "red"))
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
