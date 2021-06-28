import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        list1 = solution.SinglyLinkedList()
        for i in [1, 2, 3]:
            list1.insert_node(i)
        list2 = solution.SinglyLinkedList()
        for i in [3, 4]:
            list2.insert_node(i)
        list3 = solution.mergeLists(list1.head, list2.head)
        outputs = [1, 2, 3, 3, 4]
        i = 0
        while list3:
            self.assertEqual(list3.data, outputs[i])
            list3 = list3.next
            i += 1

    def test_case_1(self):
        list1 = solution.SinglyLinkedList()
        for i in [4, 5, 6]:
            list1.insert_node(i)
        list2 = solution.SinglyLinkedList()
        for i in [1, 2, 10]:
            list2.insert_node(i)
        list3 = solution.mergeLists(list1.head, list2.head)
        outputs = [1, 2, 4, 5, 6, 10]
        i = 0
        while list3:
            self.assertEqual(list3.data, outputs[i])
            list3 = list3.next
            i += 1


if __name__ == '__main__':
    unittest.main()
