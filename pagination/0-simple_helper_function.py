#!/usr/bin/env python3
"""Pagination helper module."""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate start and end index for a given pagination page.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index (inclusive)
               and end index (exclusive) corresponding to the page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
