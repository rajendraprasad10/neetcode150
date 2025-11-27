import asyncio
import aiohttp
import time

URL = "http://web-lb-1733770886.us-east-1.elb.amazonaws.com/api/transaction"
TOTAL_REQUESTS = 50000
CONCURRENCY = 500     # number of parallel tasks


async def fetch(session):
    """Send a GET request and return status."""
    try:
        async with session.get(URL) as response:
            return response.status
    except Exception as e:
        return f"ERROR: {e}"


async def worker(name, session, queue, results):
    """Worker task to perform requests."""
    while not queue.empty():
        _ = await queue.get()
        status = await fetch(session)
        results.append(status)
        queue.task_done()


async def main():
    start = time.time()

    queue = asyncio.Queue()
    for i in range(TOTAL_REQUESTS):
        queue.put_nowait(i)

    results = []

    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(worker(i, session, queue, results))
            for i in range(CONCURRENCY)
        ]

        await queue.join()

        for task in tasks:
            task.cancel()

    end = time.time()

    print("----- Load Test Summary -----")
    print(f"Total Requests: {TOTAL_REQUESTS}")
    print(f"Time Taken: {end - start:.2f} sec")
    print(f"Success: {results.count(200)}")
    print(f"Failures: {TOTAL_REQUESTS - results.count(200)}")


if __name__ == "__main__":
    asyncio.run(main())
