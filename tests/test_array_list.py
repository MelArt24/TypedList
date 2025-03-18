import unittest
from TypedList.src.array_list import ArrayList


class TestArrayList(unittest.TestCase):
    def test_append(self):
        arr = ArrayList()
        arr.append('A')
        self.assertEqual(arr.get(0), 'A')

    def test_insert(self):
        arr = ArrayList()
        arr.append('A')
        arr.insert('B', 1)
        self.assertEqual(arr.get(1), 'B')

    def test_delete(self):
        arr = ArrayList()
        arr.append('A')
        arr.append('B')
        arr.delete(0)
        self.assertEqual(arr.get(0), 'B')

    def test_deleteAll(self):
        arr = ArrayList()
        arr.append('A')
        arr.append('B')
        arr.append('A')
        arr.deleteAll('A')
        self.assertEqual(arr.length(), 1)

    def test_clone(self):
        arr = ArrayList()
        arr.append('A')
        arr.append('B')
        cloned = arr.clone()
        self.assertEqual(cloned.get(0), 'A')

    def test_reverse(self):
        arr = ArrayList()
        arr.append('1')
        arr.append('2')
        arr.reverse()
        self.assertEqual(arr.get(0), '2')

    def test_findFirst(self):
        arr = ArrayList()
        arr.append('A')
        arr.append('B')
        self.assertEqual(arr.findFirst('A'), 0)

    def test_findLast(self):
        arr = ArrayList()
        arr.append('A')
        arr.append('B')
        self.assertEqual(arr.findLast('A'), 0)

    def test_clear(self):
        arr = ArrayList()
        arr.append('A')
        arr.clear()
        self.assertEqual(arr.length(), 0)

    def test_extend(self):
        arr = ArrayList()
        arr.append('A')
        new_list = ArrayList()
        new_list.append('B')
        arr.extend(new_list)
        self.assertEqual(arr.length(), 2)


if __name__ == "__main__":
    unittest.main()
