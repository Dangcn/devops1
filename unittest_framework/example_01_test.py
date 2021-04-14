import unittest
from time import sleep


class Test_fmk(unittest.TestCase):
    '''
    unittest framework for example
    '''

    def test_01(self):
        a = 2
        sleep(2)
        self.assertEqual(a, 2)

    def test_02(self):
        self.assertTrue(False)


