#!/usr/bin/env python3
"""
executing multiple coroutines
at the same time
"""
import asyncio
from typing import List
from 0-basic_async_syntax.py import wait_random
"""
importing required modules
and files
"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    coroutines functions
    running cocurrently
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
