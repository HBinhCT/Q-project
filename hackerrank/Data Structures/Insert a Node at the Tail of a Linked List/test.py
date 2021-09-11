import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        inputs = [141, 302, 164, 530, 474]
        outputs = [141, 302, 164, 530, 474]
        linked_list = solution.SinglyLinkedList()
        for item in inputs:
            linked_list.head = solution.insertNodeAtTail(linked_list.head, item)
        node = linked_list.head
        i = 0
        while node:
            self.assertEqual(node.data, outputs[i])
            node = node.next
            i += 1

    def test_case_1(self):
        inputs = [236, 326, 937]
        outputs = [236, 326, 937]
        linked_list = solution.SinglyLinkedList()
        for item in inputs:
            linked_list.head = solution.insertNodeAtTail(linked_list.head, item)
        node = linked_list.head
        i = 0
        while node:
            self.assertEqual(node.data, outputs[i])
            node = node.next
            i += 1


if __name__ == '__main__':
    unittest.main()
