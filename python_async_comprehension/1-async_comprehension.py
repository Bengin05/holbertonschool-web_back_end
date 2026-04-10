#!/usr/bin/env python3
"""Module that defines an asynchronous comprehension coroutine."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect random numbers from an async generator into a list.

    This coroutine asynchronously iterates over values produced by
    `async_generator` and returns them as a list of floats.

    Returns:
        List[float]: A list of random floating-point numbers.
    """
    return [i async for i in async_generator()]
