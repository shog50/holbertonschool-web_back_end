#!/usr/bin/env python3
"""
Module that provides a function to sum a list containing ints and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing both integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of numbers (ints and floats).

    Returns:
        float: The sum of all elements as a float.
    """
    return sum(mxd_lst)
