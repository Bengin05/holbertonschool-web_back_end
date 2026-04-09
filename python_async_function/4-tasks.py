#!/usr/bin/env python3
"""
Module to create and run multiple asyncio wait_random tasks concurrently.

This module imports the wait_random coroutine from 0-basic_async_syntax
and the task_wait_random function from 3-tasks. It provides an
asynchronous function task_wait_n that runs n tasks concurrently
and collects their delays in the order they complete.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run n wait_random tasks concurrently and collect their results.

    Creates n asyncio tasks using task_wait_random with a given
    max_delay, waits for them to complete in the order they finish,
    and returns a list of the results.

    Args:
        n (int): Number of tasks to create.
        max_delay (int): Maximum delay for each wait_random task.

    Returns:
        List[float]: List of delays returned by each task, in the order
                     they completed.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
