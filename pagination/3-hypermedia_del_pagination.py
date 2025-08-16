#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
from typing import List, Dict, Any, Optional


class Server:
    """
    Server class to paginate a database of popular baby names
    with deletion-resilient hypermedia pagination.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with no dataset loaded yet."""
        self.__dataset: Optional[List[List[str]]] = None
        self.__indexed_dataset: Optional[Dict[int, List[str]]] = None

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
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """
        Return the dataset indexed by sorting position, starting at 0.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self,
        index: int = None,
        page_size: int = 10
    ) -> Dict[str, Any]:
        """
        Return a dictionary with deletion-resilient hypermedia pagination.

        Args:
            index (int): The start index for the current page.
            page_size (int): Number of records per page.

        Returns:
            Dict[str, Any]: {
                'index': current start index,
                'next_index': index to query next,
                'page_size': number of items returned,
                'data': list of dataset rows
            }
        """
        assert isinstance(index, int) and index >= 0
        indexed_data = self.indexed_dataset()
        max_index = max(indexed_data.keys())
        assert index <= max_index

        data: List[List[str]] = []
        current_index: int = index

        # Skip missing indexes and collect page_size items
        while (len(data) < page_size and
               current_index <= max_index):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": current_index
        }
