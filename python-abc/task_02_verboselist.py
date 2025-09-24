#!/usr/bin/env python3
"""
Extending the Python List with Notifications
"""

from typing import SupportsIndex

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        num_items = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {num_items} items.")

    def remove(self, item):
        print(f"Removed {item} from the list.")
    def pop(self, index: SupportsIndex = -1):
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
        print(f"Popped {item} from the list.")
        return super().pop(index)
