import unittest
from basiccalc import calc

class testcalc(unittest.TestCase):

    def testsum(self):
        calctest = calc(8, 2)
        self.assertEqual(calctest.getsum(), 10, 'The sum is wrong.')

    def testdiff(self):
        calctest = calc(8, 2)
        self.assertEqual(calctest.getdiff(), 6, 'The difference is wrong.')

    def testmult(self):
        calctest = calc(8, 2)
        self.assertEqual(calctest.getmult(), 16, 'The multiple is wrong.')
    
    def testlarge(self):
        calctest = calc(8,2)
        self.assertEqual(calctest.getlarge(), 8, 'The larger is wrong.')

if __name__ == '__main__':
    unittest.main()