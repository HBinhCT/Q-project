import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        inputs = [16, 13, 7]
        outputs = [16, 13, 1, 7]
        linked_list = solution.SinglyLinkedList()
        for item in inputs:
            linked_list.insert_node(item)
        node = solution.insertNodeAtPosition(linked_list.head, 1, 2)
        i = 0
        while node:
            self.assertEqual(node.data, outputs[i])
            node = node.next
            i += 1

    def test_case_1(self):
        inputs = [11, 9, 19, 10, 4]
        outputs = [11, 9, 19, 20, 10, 4]
        linked_list = solution.SinglyLinkedList()
        for item in inputs:
            linked_list.insert_node(item)
        node = solution.insertNodeAtPosition(linked_list.head, 20, 3)
        i = 0
        while node:
            self.assertEqual(node.data, outputs[i])
            node = node.next
            i += 1

    def test_case_2(self):
        inputs = [1, 2, 3, 4, 5, 6]
        outputs = [1, 2, 3, 4, 5, 7, 6]
        linked_list = solution.SinglyLinkedList()
        for item in inputs:
            linked_list.insert_node(item)
        node = solution.insertNodeAtPosition(linked_list.head, 7, 5)
        i = 0
        while node:
            self.assertEqual(node.data, outputs[i])
            node = node.next
            i += 1


if __name__ == '__main__':
    unittest.main()
