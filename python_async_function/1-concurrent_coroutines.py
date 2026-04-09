#!/usr/bin/env python3
"""Async utilities for running multiple random delays concurrently."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple asynchronous wait_random calls concurrently.

    This function launches `n` coroutines of wait_random with the same
    maximum delay and collects their results in the order they complete.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay passed to each wait_random call.

    Returns:
        List[float]: A list of delays in seconds, ordered by completion time.
    """
    coroutine = [wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for coro in asyncio.as_completed(coroutine):
        delays.append(await coro)
    return delays
