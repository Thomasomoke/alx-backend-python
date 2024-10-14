#!/usr/bin/env python3
"""
asynchronous coroutine that takes in an integer
with a default valuethat wats fr a random delay
"""
import asyncio
import random
"""
random module generates random numners
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    function takes an integer
    waits a random delay before returning
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
