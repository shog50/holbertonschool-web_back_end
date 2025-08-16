#!/usr/bin/env python3
"""
Module that provides hypermedia pagination
for a dataset of popular baby names.
"""
import csv
import math
from typing import List, Dict, Any, Optional


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with no dataset loaded yet."""
        self.__dataset: Optional[List[List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """
        Return the cached dataset.
        If not already loaded, read from the CSV file
        and cache the content, skipping the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Return a specific page of the dataset.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of records per page.

        Returns:
            List[List[str]]: A list of rows from the dataset
            corresponding to the requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start: int = (page - 1) * page_size
        end: int = start + page_size
        data: List[List[str]] = self.dataset()
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return pagination information with hypermedia metadata.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of records per page.

        Returns:
            Dict[str, Any]: A dictionary containing:
                - page_size: length of the returned page
                - page: current page number
                - data: dataset page (list of rows)
                - next_page: number of the next page, None if not available
                - prev_page: number of the previous page, None if not available
                - total_pages: total number of pages
        """
        data: List[List[str]] = self.get_page(page, page_size)
        total_items: int = len(self.dataset())
        total_pages: int = math.ceil(total_items / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
