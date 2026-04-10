#!/usr/bin/env python3
"""Module that measures the runtime of asynchronous comprehensions."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure total execution time of concurrent async comprehensions.

    This coroutine runs `async_comprehension` four times concurrently
    using `asyncio.gather` and returns the total elapsed time.

    Returns:
        float: The total execution time in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
