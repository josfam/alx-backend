#!/usr/bin/env python3

"""Class and function setup to demonstrate basic pagination"""

import csv
import math
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Takes a page number and a page size and returns a tuple of the range
    of pages to page through

    Args:
        page: The current page number (1-indexed)
        page_size: The number of items on a single page

    Returns:
        A tuple representing the start and end index of the range of indices
        in the list for that particular page in the pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets the requested range of contents from the requested page.

        Args:
            page: The page number whose contents to retrieve
            page_size: The number of items to show on a page

        Returns:
            The requested contents as a list of lists

        Raises:
            AssertionError: If page and page_size are not integers that are
                            greater than 0
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        try:
            # test out of bouds
            first, last = dataset[start], dataset[end]
        except IndexError:
            return []
        return dataset[start:end]
