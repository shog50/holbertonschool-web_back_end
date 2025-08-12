#!/usr/bin/env python3
"""
This module provides a Server class for paginating a dataset of
popular baby names from a CSV file, along with a helper function
to determine index ranges for pagination.
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for a given pagination request.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and
        the end index for the requested page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.
    The dataset is loaded from a CSV file and cached for reuse.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the Server instance with an empty dataset cache."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file.

        Returns:
            List[List]: The dataset without the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Remove header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of the dataset.

        Args:
            page (int): The current page number (must be a positive integer).
            page_size (int): The number of rows per page (must be a positive
                             integer).

        Returns:
            List[List]: The list of rows for the requested page.
                        Returns an empty list if the page is out of range.

        Raises:
            AssertionError: If page or page_size are not positive integers.
        """
        # Validate inputs
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Determine start and end indexes
        start, end = index_range(page, page_size)

        dataset = self.dataset()

        # Return empty list if start index is out of range
        if start >= len(dataset):
            return []

        return dataset[start:end]
