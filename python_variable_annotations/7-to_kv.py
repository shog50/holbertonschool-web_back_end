#!/usr/bin/env python3
"""
Module that provides a function to return a tuple with a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string and the square of the number (as float).

    Args:
        k (str): A string key.
        v (Union[int, float]): A number (int or float).

    Returns:
        Tuple[str, float]: A tuple with k and the square of v as float.
    """
    return (k, float(v ** 2))
