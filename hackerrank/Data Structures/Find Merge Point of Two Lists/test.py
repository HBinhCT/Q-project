import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        index = 1
        list1_count = 3
        list1 = solution.SinglyLinkedList()
        for item in [1, 2, 3]:
            list1.insert_node(item)
        list2_count = 1
        list2 = solution.SinglyLinkedList()
        for item in [1]:
            list2.insert_node(item)
        ptr1 = list1.head
        ptr2 = list2.head
        for i in range(list1_count):
            if i < index:
                ptr1 = ptr1.next
        for i in range(list2_count):
            if i != list2_count - 1:
                ptr2 = ptr2.next
        ptr2.next = ptr1
        self.assertEqual(solution.findMergeNode(list1.head, list2.head), 2)

    def test_case_1(self):
        index = 2
        list1_count = 3
        list1 = solution.SinglyLinkedList()
        for item in [1, 2, 3]:
            list1.insert_node(item)
        list2_count = 1
        list2 = solution.SinglyLinkedList()
        for item in [1]:
            list2.insert_node(item)
        ptr1 = list1.head
        ptr2 = list2.head
        for i in range(list1_count):
            if i < index:
                ptr1 = ptr1.next
        for i in range(list2_count):
            if i != list2_count - 1:
                ptr2 = ptr2.next
        ptr2.next = ptr1
        self.assertEqual(solution.findMergeNode(list1.head, list2.head), 3)


if __name__ == '__main__':
    unittest.main()
