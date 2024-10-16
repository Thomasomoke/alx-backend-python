#!/usr/bin/env python3
"""
a measure_runtime coroutine that will execute
async_comprehension four times
in parallel using asyncio.gather
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time = time.perf_counter()
    """
    executes async_comprehension
    four times in parallel
    """
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
        )
    end_time = time.perf_counter()
    return end_time - start_time
