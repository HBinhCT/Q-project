import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        inputs = [1, 2, 3, 4, 5]
        outputs = [5, 4, 3, 2, 1]
        linked_list = solution.SinglyLinkedList()
        for item in inputs:
            linked_list.insert_node(item)
        node = solution.reverse(linked_list.head)
        i = 0
        while node:
            self.assertEqual(node.data, outputs[i])
            node = node.next
            i += 1

    def test_case_1(self):
        inputs = [3, 4, 2, 5]
        outputs = [5, 2, 4, 3]
        linked_list = solution.SinglyLinkedList()
        for item in inputs:
            linked_list.insert_node(item)
        node = solution.reverse(linked_list.head)
        i = 0
        while node:
            self.assertEqual(node.data, outputs[i])
            node = node.next
            i += 1


if __name__ == '__main__':
    unittest.main()
