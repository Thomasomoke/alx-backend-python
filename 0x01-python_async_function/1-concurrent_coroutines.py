#!/usr/bin/env python3
"""
executing multiple coroutines
at the same time
"""
import asyncio
from typing import List
from basic_async_syntax import wait_random
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
    return insertion_sort(delays)


def insertion_sort(arr: List[float]) -> List[float]:
    """
    perform insertion sort on
    a list of values
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
