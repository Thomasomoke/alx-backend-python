#!/usr/bin/env python3
"""
 coroutine called async_comprehension
 collect 10 random numbers
 return the numbers
"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator
"""
importing relevant modules
and files
"""


async def async_comprehension() -> List[float]:
    """
    async comprehensions
    using asyncgenerator
    """
    numbers = [i async for i in async_generator()]
    return numbers
