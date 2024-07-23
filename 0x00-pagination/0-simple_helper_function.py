#!/usr/bin/env python3

"""
    FUNCTION TO HELP FUTURE PAGINATIONS
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        CALCULATES INDEX USING THIS FORMULA:
        1. start_index = (page - 1) * page_size
        2. end_index = start_index + page_size
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
