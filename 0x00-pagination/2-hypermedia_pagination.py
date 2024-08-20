#!/usr/bin/env python3
'''
pagination module'''

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    '''
    This is a simple helper function
    Returns a tuple of the page and page size
    '''

    starting_index = (page - 1) * page_size
    ending_index = page * page_size

    return (starting_index, ending_index)


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
        get_page use index_range to find the correct indexes to paginate
        the dataset correctly

        Returns the appropriate page of the dataset

        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Hypermedia pagination
        Returns a key value pair
        """
        dataset = self.dataset()

        total_items = len(dataset)
        total_pages = math.ceil(total_items / page_size)

        data = self.get_page(page, page_size)
        page_size = len(data)

        metadata = {
                "page_size": page_size,
                "page": page,
                "data": data,
                "next_page": page + 1 if page < total_pages else None,
                "prev_page": page - 1 if page > 1 else None,
                "total_pages": total_pages
                }
        return metadata


