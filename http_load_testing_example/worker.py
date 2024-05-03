"""
TODO
"""

import logging

import aiohttp

logger = logging.getLogger(__name__)

class Worker:
    """A single automated endpoint user (for load-testing)"""

    def __init__(self, id: str, lifetime: int, session: aiohttp.ClientSession) -> None:
        """Define attributes at instantiation"""
        self.id = id
        self.session = session
        self.request_count = 0
        self.lifetime = lifetime

    async def work(self):
        """
        Repeatedly use the endpoints according to specified logic
        """
        while self.request_count < self.lifetime:
            async with self.session.get("http://localhost:5000/get_task") as resp:
                self.request_count += 1
                logger.info(
                    "worker [%s] request [%s] to /get_task", self.id, self.request_count
                )
                logger.info(
                    "worker [%s] request [%s] had status %s",
                    self.id,
                    self.request_count,
                    resp.status,
                )
                task = await resp.text()
                logger.info(
                    "worker [%s] request [%s] received task %s",
                    self.id,
                    self.request_count,
                    task,
                )


