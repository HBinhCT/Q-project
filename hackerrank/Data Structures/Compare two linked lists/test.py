import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        list1 = solution.SinglyLinkedList()
        for i in [1, 2]:
            list1.insert_node(i)
        list2 = solution.SinglyLinkedList()
        for i in [1, 1]:
            list2.insert_node(i)
        self.assertEqual(solution.compare_lists(list1.head, list2.head), 0)
        list1 = solution.SinglyLinkedList()
        for i in [1, 2]:
            list1.insert_node(i)
        list2 = solution.SinglyLinkedList()
        for i in [1, 2]:
            list2.insert_node(i)
        self.assertEqual(solution.compare_lists(list1.head, list2.head), 1)

    def test_case_1(self):
        list1 = solution.SinglyLinkedList()
        for i in [3, 2, 2]:
            list1.insert_node(i)
        list2 = solution.SinglyLinkedList()
        for i in [3, 2, 2]:
            list2.insert_node(i)
        self.assertEqual(solution.compare_lists(list1.head, list2.head), 1)
        list1 = solution.SinglyLinkedList()
        for i in [2, 1]:
            list1.insert_node(i)
        list2 = solution.SinglyLinkedList()
        for i in [1, 2]:
            list2.insert_node(i)
        self.assertEqual(solution.compare_lists(list1.head, list2.head), 0)


if __name__ == '__main__':
    unittest.main()
