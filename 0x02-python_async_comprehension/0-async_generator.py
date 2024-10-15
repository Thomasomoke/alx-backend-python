#!/usr/bin/env python3
"""
coroutine called async_generator that takes no arguments
loop 10 times, each time asynchronously wait 1 second
"""
import asyncio
import random
from typing import AsyncGenerator
"""
importing the relevant modules
"""


async def async_generator() -> AsyncGenerator[float, None]:
    for i in range(10):
        await asyncio.sleep(1)
        """generate random numbers
        between 0 and 10
        """
        yield random.uniform(0, 10)
