import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        linked_list = solution.SinglyLinkedList()
        for item in [1]:
            linked_list.insert_node(item)
        self.assertEqual(solution.getNode(linked_list.head, 0), 1)
        linked_list = solution.SinglyLinkedList()
        for item in [3, 2, 1]:
            linked_list.insert_node(item)
        self.assertEqual(solution.getNode(linked_list.head, 2), 3)

    def test_case_1(self):
        linked_list = solution.SinglyLinkedList()
        for item in [4, 3, 2, 1]:
            linked_list.insert_node(item)
        self.assertEqual(solution.getNode(linked_list.head, 2), 3)


if __name__ == '__main__':
    unittest.main()
