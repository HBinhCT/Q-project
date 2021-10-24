import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '10',
        'Donald Trump becomes the 45th #US President',
        'Potentially habitable exoplanet #ProximaB discovered',
        '#RogerFederer wins #US Open for 5th time',
        '#GravitationalWaves detection successful',
        'Traces of liquid water discovered on #Mars',
        'Life Could Survive on Exoplanet #ProximaB',
        'Go go #RogerFederer',
        'Ten ways #ProximaB is different from Earth',
        'ISRO becomes 4th space agency to reach #Mars',
        '#RogerFederer beats #Nadal',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '#ProximaB\n' +
                         '#RogerFederer\n' +
                         '#Mars\n' +
                         '#US\n' +
                         '#GravitationalWaves\n')


if __name__ == '__main__':
    unittest.main()
