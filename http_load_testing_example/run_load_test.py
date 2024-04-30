"""
TODO

Example Usage:
$ poetry run python run_load_test.py
"""

import asyncio

import aiohttp

import load_test_config
from worker import Worker


async def main():
    async with aiohttp.ClientSession() as session:
        workers: list[Worker] = [Worker(id=idx, session=session) for idx in range(69)]
        # async with session.get("http://httpbin.org/get") as resp:
        #    print(resp.status)
        #    print(await resp.text())


if __name__ == "__main__":
    asyncio.run(main())
