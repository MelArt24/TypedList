import unittest

from src.doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def test_append(self):
        dll = DoublyLinkedList()
        dll.append('A')
        dll.append('B')
        dll.append('C')
        self.assertEqual(str(dll), "A B C")

    def test_insert(self):
        dll = DoublyLinkedList()
        dll.append('A')
        dll.append('C')
        dll.insert('B', 1)
        self.assertEqual(str(dll), "A B C")

    def test_delete(self):
        dll = DoublyLinkedList()
        dll.append('A')
        dll.append('B')
        dll.append('C')
        self.assertEqual(dll.delete(1), 'B')
        self.assertEqual(str(dll), "A C")

    def test_deleteAll(self):
        dll = DoublyLinkedList()
        dll.append('A')
        dll.append('B')
        dll.append('A')
        dll.deleteAll('A')
        self.assertEqual(str(dll), "B")

    def test_get(self):
        dll = DoublyLinkedList()
        dll.append('X')
        dll.append('Y')
        dll.append('Z')
        self.assertEqual(dll.get(1), 'Y')

    def test_clone(self):
        dll = DoublyLinkedList()
        dll.append('A')
        dll.append('B')
        cloned = dll.clone()
        self.assertEqual(str(cloned), "A B")

    def test_reverse(self):
        dll = DoublyLinkedList()
        dll.append('1')
        dll.append('2')
        dll.append('3')
        dll.reverse()
        self.assertEqual(str(dll), "3 2 1")

    def test_findFirst(self):
        dll = DoublyLinkedList()
        dll.append('X')
        dll.append('Y')
        dll.append('X')
        self.assertEqual(dll.findFirst('X'), 0)

    def test_findLast(self):
        dll = DoublyLinkedList()
        dll.append('X')
        dll.append('Y')
        dll.append('X')
        self.assertEqual(dll.findLast('X'), 2)

    def test_clear(self):
        dll = DoublyLinkedList()
        dll.append('A')
        dll.append('B')
        dll.clear()
        self.assertEqual(str(dll), "")

    def test_extend(self):
        dll = DoublyLinkedList()
        dll.append('1')
        dll.append('2')

        new_list = DoublyLinkedList()
        new_list.append('3')
        new_list.append('4')

        dll.extend(new_list)
        self.assertEqual(str(dll), "1 2 3 4")


if __name__ == "__main__":
    unittest.main()
