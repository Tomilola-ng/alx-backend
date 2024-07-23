#!/usr/bin/env python3

"""
    PAGINATION DELETING FUNCTION
"""

import csv
from typing import Dict, List

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
            INDEXER
        """

        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
            RETRIEVER
        """

        data = self.indexed_dataset()
        assert index is not None and 0 <= index < len(data), "Index out of range"

        page_data = []
        data_count = 0
        next_index = index

        for i in range(index, len(data)):
            if data_count < page_size:
                page_data.append(data[i])
                data_count += 1
            else:
                next_index = i
                break
        else:
            next_index = None if data_count < page_size else next_index

        page_info = {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }
        return page_info
