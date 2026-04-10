#!/usr/bin/env python3
"""Module that defines an asynchronous generator producing random numbers."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronously generate random floating-point numbers.

    This coroutine yields 10 random float values between 0 and 10.
    Each value is produced after a 1-second asynchronous delay.

    Yields:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
