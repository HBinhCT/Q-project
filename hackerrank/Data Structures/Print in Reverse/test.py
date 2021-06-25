import io
import unittest
from contextlib import redirect_stdout
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            lns = [5, 3, 5]
            inputs = [
                [16, 12, 4, 2, 5],
                [7, 3, 9],
                [5, 1, 18, 3, 13],
            ]
            for i, ln in enumerate(lns):
                linked_list = solution.SinglyLinkedList()
                for j in range(ln):
                    linked_list.insert_node(inputs[i][j])
                solution.reversePrint(linked_list.head)
        self.assertEqual(text_trap.getvalue(),
                         '5\n' +
                         '2\n' +
                         '4\n' +
                         '12\n' +
                         '16\n' +
                         '9\n' +
                         '3\n' +
                         '7\n' +
                         '13\n' +
                         '3\n' +
                         '18\n' +
                         '1\n' +
                         '5\n')

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            lns = [3, 3, 4]
            inputs = [
                [11, 1, 17],
                [12, 11, 15],
                [5, 7, 15, 14],
            ]
            for i, ln in enumerate(lns):
                linked_list = solution.SinglyLinkedList()
                for j in range(ln):
                    linked_list.insert_node(inputs[i][j])
                solution.reversePrint(linked_list.head)
        self.assertEqual(text_trap.getvalue(),
                         '17\n' +
                         '1\n' +
                         '11\n' +
                         '15\n' +
                         '11\n' +
                         '12\n' +
                         '14\n' +
                         '15\n' +
                         '7\n' +
                         '5\n')


if __name__ == '__main__':
    unittest.main()
