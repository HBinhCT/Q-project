import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        inputs = [1, 3, 4, 10]
        outputs = [1, 3, 4, 5, 10]
        linked_list = solution.DoublyLinkedList()
        for item in inputs:
            linked_list.insert_node(item)
        node = solution.sortedInsert(linked_list.head, 5)
        i = 0
        while node:
            self.assertEqual(node.data, outputs[i])
            node = node.next
            i += 1

    def test_case_1(self):
        inputs = [2, 3, 4]
        outputs = [1, 2, 3, 4]
        linked_list = solution.DoublyLinkedList()
        for item in inputs:
            linked_list.insert_node(item)
        node = solution.sortedInsert(linked_list.head, 1)
        i = 0
        while node:
            self.assertEqual(node.data, outputs[i])
            node = node.next
            i += 1

    def test_case_2(self):
        inputs = [1, 2, 3]
        outputs = [1, 2, 3, 4]
        linked_list = solution.DoublyLinkedList()
        for item in inputs:
            linked_list.insert_node(item)
        node = solution.sortedInsert(linked_list.head, 4)
        i = 0
        while node:
            self.assertEqual(node.data, outputs[i])
            node = node.next
            i += 1


if __name__ == '__main__':
    unittest.main()
