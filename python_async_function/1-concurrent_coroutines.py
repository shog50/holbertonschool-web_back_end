#!/usr/bin/env python3
"""
This module defines an asynchronous routine that concurrently runs
multiple wait_random coroutines and returns their delays in ascending order.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay passed to wait_random.

    Returns:
        List[float]: List of all delays in ascending order.
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for coroutine in asyncio.as_completed(tasks):
        delay = await coroutine
        delays.append(delay)
    return delays
