#!/usr/bin/python3
"""composed of MyList Class
"""


class MyList(list):
    """MyList 
    Args:
        list (list): 
    """

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
