import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        linked_list = solution.SinglyLinkedList()
        count = -1
        for item in [1]:
            linked_list.insert_node(item)
        extra = solution.SinglyLinkedListNode(-1)
        temp = linked_list.head
        for i in range(count):
            if i == 1:
                extra = temp
            if i != count - 1:
                temp = temp.next
        temp.next = extra
        self.assertEqual(solution.has_cycle(linked_list.head), 0)

    def test_case_1(self):
        linked_list = solution.SinglyLinkedList()
        count = 3
        for item in [1, 2, 3]:
            linked_list.insert_node(item)
        extra = solution.SinglyLinkedListNode(-1)
        temp = linked_list.head
        for i in range(count):
            if i == 1:
                extra = temp
            if i != count - 1:
                temp = temp.next
        temp.next = extra
        self.assertEqual(solution.has_cycle(linked_list.head), 1)


if __name__ == '__main__':
    unittest.main()
