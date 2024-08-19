#!/usr/bin/env python3

"""A simple pagination helper method"""

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
