import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        inputs = [383, 484, 392, 975, 321]
        outputs = [321, 975, 392, 484, 383]
        linked_list = solution.SinglyLinkedList()
        for item in inputs:
            linked_list.head = solution.insertNodeAtHead(linked_list.head, item)
        node = linked_list.head
        i = 0
        while node:
            self.assertEqual(node.data, outputs[i])
            node = node.next
            i += 1

    def test_case_1(self):
        inputs = [321, 641, 653, 524, 952, 337, 955, 891, 590, 133]
        outputs = [133, 590, 891, 955, 337, 952, 524, 653, 641, 321]
        linked_list = solution.SinglyLinkedList()
        for item in inputs:
            linked_list.head = solution.insertNodeAtHead(linked_list.head, item)
        node = linked_list.head
        i = 0
        while node:
            self.assertEqual(node.data, outputs[i])
            node = node.next
            i += 1


if __name__ == '__main__':
    unittest.main()
