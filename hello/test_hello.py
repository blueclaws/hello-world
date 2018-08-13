"""sample test"""
import unittest

from hello import hello


class TestHello(unittest.TestCase):
    """sample test"""

    def test_world(self):
        """sample test"""
        self.assertEqual(3, 3)

    def test_world_unicode(self):
        """sample test with unicode"""
        self.assertEqual(4, 4)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestHello('test_div'))
    #suite.addTest(TestHello('test_func'))
    #suite.addTest(TestHello('test_imlol'))
    return suite

if __name__ == '__main__':
    #unittest.main()
    runner = unittest.TextTestRunner()
    runner.run(suite())