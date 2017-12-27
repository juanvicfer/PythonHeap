
import unittest
from MyHeap import MyHeap


class TestHeap(unittest.TestCase):
    def test_empty_after_construction(self):
        a = MyHeap()
        self.assertTrue(a.empty())

    def test_not_empty_after_adding_one_element(self):
        a = MyHeap()
        a.add(5)
        self.assertFalse(a.empty())

    def test_size_one_after_adding_one_element(self):
        a = MyHeap()
        a.add(5)
        self.assertEqual(a.size(),1)

    def test_is_empty_afer_removing_elements(self):
        a = MyHeap()
        a.add(10)
        a.remove()
        self.assertTrue(a.empty())

    def test_after_adding_one_returns_same(self):
        a = MyHeap()
        a.add(5)
        self.assertEqual(a.remove(), 5)

    def test_after_adding_two_ordered_returns_same_ordered(self):
        a = MyHeap()
        a.add(3)
        a.add(4)
        self.assertEqual(a.remove(), 3)
        self.assertEqual(a.remove(), 4)

    def test_after_adding_two_unordered_returns_same_ordered(self):
        a = MyHeap()
        a.add(4)
        a.add(3)
        self.assertEqual(a.remove(), 3)
        self.assertEqual(a.remove(), 4)

    def test_keeps_heap_property(self):
        a = MyHeap()
        a.add(4)
        a.add(2)
        a.add(7)
        a.add(3)
        a.add(5)

        self.assertEqual(a.remove(), 2)
        self.assertEqual(a.remove(), 3)
        self.assertEqual(a.remove(), 4)
        self.assertEqual(a.remove(), 5)
        self.assertEqual(a.remove(), 7)

    def test_random_remove_works(self):
        a = MyHeap()
        a.add(4)
        a.add(6)
        a.add(2)
        a.add(7)
        a.add(3)
        self.assertEqual(a.remove(),2)
        a.add(5)
        self.assertEqual(a.remove(), 3)
        self.assertEqual(a.remove(), 4)
        self.assertEqual(a.remove(), 5)
        self.assertEqual(a.remove(), 6)
        self.assertEqual(a.remove(), 7)


suite = unittest.TestLoader().loadTestsFromTestCase(TestHeap)

unittest.TextTestRunner(verbosity=2).run(suite)
