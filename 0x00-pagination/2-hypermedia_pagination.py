#!/usr/bin/env python3

"""
    A SAMPLE PAGINATION PROJECT
"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        CALCULATES INDEX USING THIS FORMULA:
        1. start_index = (page - 1) * page_size
        2. end_index = start_index + page_size
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """
        A STATIC CLASS TO ACT LIKE A DATABASE SERVER
    """

    SERVER_DB = "Popular_Baby_Names.csv"

    def __init__(self):
        """
            CREATES A NEW SERVER INSTANCE
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
            EXISTING CACHED DATASET JUST LIKE REDIS
        """

        if self.__dataset is None:
            with open(self.SERVER_DB) as csv_file:
                reader = csv.reader(csv_file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            FUNCTION TO RETRIEVE PAGES
        """

        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()


        if start > len(data):
            return []

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
            HYPER DETAILS GENERATOR AND RETRIEVER
        """

        page_data = self.get_page(page, page_size)
        start_index, end_index = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)

        page_info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if end_index < len(self.__dataset) else None,
            'prev_page': page - 1 if start_index > 0 else None,
            'total_pages': total_pages,
        }

        return page_info
