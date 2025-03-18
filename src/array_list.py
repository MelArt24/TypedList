class ArrayList:
    def __init__(self):
        self.items = []

    def length(self):
        return len(self.items)

    def append(self, element: str):
        self.items.append(element)

    def insert(self, element: str, index: int):
        if index < 0 or index > len(self.items):
            raise IndexError("Index is out of range")
        self.items.insert(index, element)

    def delete(self, index: int):
        if index < 0 or index >= len(self.items):
            raise IndexError("Index is out of range")
        return self.items.pop(index)

    def deleteAll(self, element: str):
        self.items = [item for item in self.items if item != element]

    def get(self, index: int):
        if index < 0 or index >= len(self.items):
            raise IndexError("Index is out of range")
        return self.items[index]

    def clone(self):
        new_list = ArrayList()
        new_list.items = self.items.copy()
        return new_list

    def reverse(self):
        self.items.reverse()

    def findFirst(self, element: str):
        try:
            return self.items.index(element)
        except ValueError:
            return -1

    def findLast(self, element: str):
        try:
            return len(self.items) - 1 - self.items[::-1].index(element)
        except ValueError:
            return -1

    def clear(self):
        self.items.clear()

    def extend(self, elements):
        self.items.extend(elements.items)
