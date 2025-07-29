#!/usr/bin/env python3
"""
This module defines an asynchronous generator that yields
10 random float numbers between 0 and 10 with a 1-second delay.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates 10 random numbers between 0 and 10,
    waiting 1 second between each yield.

    Yields:
        float: A random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
