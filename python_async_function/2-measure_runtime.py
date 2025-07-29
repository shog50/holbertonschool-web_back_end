#!/usr/bin/env python3
"""
Module that measures the average runtime of the wait_n coroutine.
"""

import time
import asyncio
from typing import Union

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns
    the average time per wait_random call.

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average execution time per coroutine.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
