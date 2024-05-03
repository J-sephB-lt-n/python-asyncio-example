"""
TODO

Example Usage:
$ poetry run python run_load_test.py
"""

import asyncio
import logging
import os
from typing import Final

import aiohttp

# set up python logger #
if os.path.exists("logs/loadtest.log"):
    os.remove("logs/loadtest.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("logs/loadtest.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

import load_test_config
from worker import Worker

N_WORKERS: Final[int] = 1_000

async def main():
    async with aiohttp.ClientSession() as session:
        workers: list[Worker] = [
            Worker(id=idx, lifetime=10, session=session) for idx in range(N_WORKERS)
        ]
        tasks = [worker.work() for worker in workers]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
