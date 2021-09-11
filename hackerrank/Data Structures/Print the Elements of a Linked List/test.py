import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        linked_list = solution.SinglyLinkedList()
        linked_list.insert_node(16)
        linked_list.insert_node(13)
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.printLinkedList(linked_list.head)
        self.assertEqual(text_trap.getvalue(),
                         '16\n' +
                         '13\n')

    def test_case_1(self):
        linked_list = solution.SinglyLinkedList()
        linked_list.insert_node(17)
        linked_list.insert_node(19)
        linked_list.insert_node(5)
        linked_list.insert_node(12)
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.printLinkedList(linked_list.head)
        self.assertEqual(text_trap.getvalue(),
                         '17\n' +
                         '19\n' +
                         '5\n' +
                         '12\n')


if __name__ == '__main__':
    unittest.main()
