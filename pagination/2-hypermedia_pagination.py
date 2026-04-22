#!/usr/bin/env python3
"""
Module for hypermedia pagination with Server class.
"""
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for pagination.

    Args:
        page (int): The page number (1-indexed)
        page_size (int): The number of items per page

    Returns:
        tuple: A tuple containing the start index and end index

    Example:
        >>> index_range(1, 7)
        (0, 7)
        >>> index_range(3, 15)
        (30, 45)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of the dataset.

        Args:
            page (int): The page number (default: 1)
            page_size (int): The number of items per page (default: 10)

        Returns:
            List[List]: A list of rows for the requested page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        all_data = self.dataset()
        start_index, end_index = index_range(page, page_size)
        return all_data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get a page of the dataset with hypermedia information.

        Args:
            page (int): The page number (default: 1)
            page_size (int): The number of items per page (default: 10)

        Returns:
            Dict: A dictionary containing:
                - page_size: the length of the returned dataset page
                - page: the current page number
                - data: the dataset page
                - next_page: number of the next page, None if no next page
                - prev_page: number of the previous page, None if no previous
                page
                - total_pages: the total number of pages in the dataset
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)

        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        if (page < total_pages):
            next_page = page + 1
        else:
            next_page = None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
