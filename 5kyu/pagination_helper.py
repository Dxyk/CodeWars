class PaginationHelper:
    """
    Take in an array of values and an integer indicating how many items will be
    allowed per each page. The types of values are not relevant.
    """

    def __init__(self, collection, items_per_page):
        """
        Initiate the pagination helper.

        :param collection: the collection of values
        :type collection: list
        :param items_per_page: items allowed per page
        :type items_per_page: int
        :return: pagination helper
        :rtype: PaginationHelper

        >>> helper = PaginationHelper(['a','b','c','d','e','f'], 4)
        >>> helper.collection
        ['a','b','c','d','e','f']
        >>> helper.item_per_page
        4
        """
        self.collection, self.item_per_page = collection, items_per_page

    def item_count(self):
        """
        Count the item number in total.

        :return: the total number of items
        :rtype: int

        >>> helper = PaginationHelper(['a','b','c','d','e','f'], 4)
        >>> helper.item_count()
        6
        """
        return len(self.collection)

    def page_count(self):
        """
        count the total page numbers.

        :return: total page numbers
        :rtype: int

        >>> helper = PaginationHelper(['a','b','c','d','e','f'], 4)
        >>> helper.page_count()
        2
        """
        page = len(self.collection) / self.item_per_page
        return int(page) if float(page).is_integer() else int(page) + 1

    def page_item_count(self, page_index):
        """
        Return number of item on the page_index, starting from 0. Return -1 if
        index out of range.

        :param page_index: page index
        :type page_index: int
        :return: number of item in this page
        :rtype: int

        >>> helper = PaginationHelper(['a','b','c','d','e','f'], 4)
        >>> helper.page_item_count(0)
        4
        >>> helper.page_item_count(1)
        2
        >>> helper.page_item_count(2)
        -1
        """
        if 0 <= page_index < self.page_count() - 1:
            return self.item_per_page
        elif page_index + 1 == self.page_count():
            return self.item_count() % self.item_per_page
        else: return -1

    def page_index(self, item_index):
        """
        Return the page index of the item index if item in the collection, else
        return -1
        :param item_index: item index
        :type item_index: int
        :return: page index
        :rtype: int

        >>> helper = PaginationHelper(['a','b','c','d','e','f'], 4)
        >>> helper.page_index(5)
        1
        >>> helper.page_index(2)
        0
        >>> helper.page_index(20)
        -1
        >>> helper.page_index(-10)
        -1
        """
        if 0 <= item_index <= self.item_count() - 1:
            for page in range(self.page_count()):
                if (page * self.item_per_page + item_index % self.item_per_page
                        == item_index):
                    return page
        else:
            return -1
