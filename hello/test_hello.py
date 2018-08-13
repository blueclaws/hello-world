"""sample test"""
import unittest

from hello import hello


class TestHello(unittest.TestCase):
    """sample test"""

    def test_three(self):
        """sample test"""
        self.assertEqual(3, 3)

    def test_four(self):
        """sample test with unicode"""
        self.assertEqual(4, 4)

