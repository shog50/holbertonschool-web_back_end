#!/usr/bin/env python3
"""
This module contains a helper function for pagination index calculation.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of (start_index, end_index) for pagination.

    The returned tuple represents the range of indexes corresponding
    to the given page number and page size.

    Page numbers are 1-indexed (i.e., first page is 1).

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
                         and end index (exclusive).
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
