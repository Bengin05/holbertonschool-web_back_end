#!/usr/bin/env python3
"""Module for measuring execution time of asynchronous functions."""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time of wait_n.

    This function records the total time taken to execute wait_n
    with `n` concurrent calls and computes the average time per call.

    Args:
        n (int): The number of coroutines to run.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The average execution time per coroutine in seconds.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
