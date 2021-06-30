import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        inputs = [1, 2, 2, 3, 4]
        outputs = [1, 2, 3, 4]
        linked_list = solution.SinglyLinkedList()
        for item in inputs:
            linked_list.insert_node(item)
        node = solution.removeDuplicates(linked_list.head)
        i = 0
        while node:
            self.assertEqual(node.data, outputs[i])
            node = node.next
            i += 1

    def test_case_1(self):
        inputs = [3, 3, 3, 4, 5, 5]
        outputs = [3, 4, 5]
        linked_list = solution.SinglyLinkedList()
        for item in inputs:
            linked_list.insert_node(item)
        node = solution.removeDuplicates(linked_list.head)
        i = 0
        while node:
            self.assertEqual(node.data, outputs[i])
            node = node.next
            i += 1


if __name__ == '__main__':
    unittest.main()
