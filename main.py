"""
The main entry script
"""

import asyncio
from worker import AsyncWorker


async def main():
    workers: list[AsyncWorker] = [
        AsyncWorker(name="Joe", continue_prob=0.8),
        AsyncWorker(name="Peter", continue_prob=0.8),
        AsyncWorker(name="Johann", continue_prob=0.8),
        AsyncWorker(name="Danny", continue_prob=0.8),
        AsyncWorker(name="Chris", continue_prob=0.8),
    ]

    worker_tasks = [worker.work() for worker in workers]

    await asyncio.gather(*worker_tasks)

    for worker in workers:
        print(worker.name, worker.accumulated)


if __name__ == "__main__":
    asyncio.run(main())
