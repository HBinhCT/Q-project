import io
import unittest
from unittest.mock import patch


class TestQ(unittest.TestCase):
    def test_case_0(self):
        with patch('builtins.input', side_effect=['4', '2', '3', '4', '1']):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                import solution
            self.assertEqual(fake_stdout.getvalue(), '2 3 4 1 ')


if __name__ == '__main__':
    unittest.main()
