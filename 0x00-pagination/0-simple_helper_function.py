#!/usr/bin/env python3
'''
pagination module'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    '''
    This is a simple helper function
    Returns a tuple of the page and page size
    '''

    starting_index = (page - 1) * page_size
    ending_index = page * page_size

    return (starting_index, ending_index)
