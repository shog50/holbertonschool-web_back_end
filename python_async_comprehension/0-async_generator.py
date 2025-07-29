#!/usr/bin/env python3
"""Coroutine that yields 10 random numbers betwn 0 and 10, one every second"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yields a random float between 0 and 10 every second, 10 times."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
