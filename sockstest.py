from socks import matchingSocks
import unittest

class testcase(unittest.TestCase):
    #Testing with 10 socks items with 4 pairs
    def test_case_one(self):
        self.assertEqual(matchingSocks(10, [1,2,1,3,4,2,5,4,1,3]), 4)
    #Testing case where there is only one sock meaning zero pair
    def test_case_two(self):
        self.assertEqual(matchingSocks(1, [1]), 0)
    #Testing case where all socks are identical but oddly numbered
    def test_case_three(self):
        self.assertEqual(matchingSocks(5, [1,1,1,1,1]), 2)
    #Testing case where there are many socks but no pair exists
    def test_case_four(self):
        self.assertEqual(matchingSocks(8, [2,3,4,5,6,7,8,9]), 0)


if __name__ == "__main__":
    unittest.main()
