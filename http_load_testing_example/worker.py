"""
TODO
"""

import aiohttp

class Worker:
    def __init__(self, id: str, session: aiohttp.ClientSession) -> None:
        self.id = id
        self.session = session

