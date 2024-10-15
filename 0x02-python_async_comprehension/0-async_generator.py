#!/usr/bin/env python3
"""
coroutine called async_generator that takes no arguments
loop 10 times, each time asynchronously wait 1 second
then yield a random number between 0 and 10
"""
import asyncio
import random
"""
importing the relevant modules
"""


async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        """generate random numbers"""
        yield random.uniform(0, 10)
