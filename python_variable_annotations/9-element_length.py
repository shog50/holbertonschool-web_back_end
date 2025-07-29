#!/usr/bin/env python3
"""
Module that provides a function to get element length from iterable
sequences.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element in the iterable
    and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences (like strings
        or lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples with each element
        and its length.
    """
    return [(i, len(i)) for i in lst]
