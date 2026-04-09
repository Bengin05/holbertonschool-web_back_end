#!/usr/bin/env python3
"""Async utilities for generating random delays."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay and return the delay duration.

    Args:
        max_delay (int): The maximum possible delay in seconds.
            Defaults to 10.

    Returns:
        float: The actual delay time in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
