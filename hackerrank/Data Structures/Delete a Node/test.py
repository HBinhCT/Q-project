import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        inputs = [20, 6, 2, 19, 7, 4, 15, 9]
        outputs = [20, 6, 2, 7, 4, 15, 9]
        linked_list = solution.SinglyLinkedList()
        for item in inputs:
            linked_list.insert_node(item)
        node = solution.deleteNode(linked_list.head, 3)
        i = 0
        while node:
            self.assertEqual(node.data, outputs[i])
            node = node.next
            i += 1

    def test_case_1(self):
        inputs = [11, 9, 2, 9]
        outputs = [11, 2, 9]
        linked_list = solution.SinglyLinkedList()
        for item in inputs:
            linked_list.insert_node(item)
        node = solution.deleteNode(linked_list.head, 1)
        i = 0
        while node:
            self.assertEqual(node.data, outputs[i])
            node = node.next
            i += 1


if __name__ == '__main__':
    unittest.main()
