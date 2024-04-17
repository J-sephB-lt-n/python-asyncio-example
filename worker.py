"""
Defines the AsyncWorker class
"""

import asyncio
import datetime
import random

now = datetime.datetime.now


class AsyncWorker:
    def __init__(self, name: str, continue_prob: float) -> None:
        self.name = name
        self.accumulated: list[int] = []
        self.continue_prob = continue_prob

    async def work(self) -> None:
        while True:
            print(
                now().time(),
                f"worker '{self.name}' started task {len(self.accumulated)+1}",
            )
            await asyncio.sleep(random.uniform(1, 5))
            self.accumulated.append(random.choice(range(1, 10)))
            print(
                now().time(),
                f"worker '{self.name}' completed task {len(self.accumulated)}",
            )
            if random.uniform(0, 1) > self.continue_prob:
                print(
                    now().time(),
                    f"""worker '{self.name}' stopped working
    worker '{self.name}' completed {len(self.accumulated)} tasks
    worker '{self.name}' accummulated a total value of {sum(self.accumulated)}""",
                )
                break
