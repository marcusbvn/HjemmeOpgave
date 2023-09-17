import unittest

from lib import Rational

class optest(unittest.TestCase):
    def test_reduce(self):
        a = Rational(5, 25)
        self.assertEqual(str(a.reduce()),"1/5")
        a = Rational(7, 15)
        self.assertEqual(str(a.reduce()),"7/15")
        a = Rational(111, 333)
        self.assertEqual(str(a.reduce()),"1/3")

    def test_negate(self):
        a = Rational(-5, 25)
        self.assertEqual(str(a.negate()),"5/25")
        a = Rational(7, -15)
        self.assertEqual(str(a.negate()),"7/15")
        a = Rational(111, 333)
        self.assertEqual(str(a.negate()),"-111/333")

    def test_invert(self):
        a = Rational(5, 25)
        self.assertEqual(str(a.invert()),"25/5")
        a = Rational(7, 15)
        self.assertEqual(str(a.invert()),"15/7")
        a = Rational(111, 333)
        self.assertEqual(str(a.invert()),"333/111")

    def test_add(self):
        a = Rational(1, 5)
        b = Rational(2, 5)
        self.assertEqual(str(a.add(b)),"15/25")
        a = Rational(3, 7)
        b = Rational(8, 3)
        self.assertEqual(str(a.add(b)),"65/21")
        a = Rational(3,4)
        b = Rational(-1,4)
        self.assertEqual(str(a.add(b)),"8/16")

    def test_sub(self):
        a = Rational(1, 5)
        b = Rational(2, 5)
        self.assertEqual(str(a.sub(b)),"-5/25")
        a = Rational(3, 7)
        b = Rational(8, 3)
        self.assertEqual(str(b.sub(a)),"47/21")
        a = Rational(3,4)
        b = Rational(-1,4)
        self.assertEqual(str(a.sub(b)),"16/16")

    def test_mul(self):
        a = Rational(1, 5)
        b = Rational(2, 5)
        self.assertEqual(str(a.mul(b)),"2/25")
        a = Rational(3, 7)
        b = Rational(8, 3)
        self.assertEqual(str(a.mul(b)),"24/21")
        a = Rational(3,4)
        b = Rational(-1,4)
        self.assertEqual(str(a.mul(b)),"-3/16")

    def test_div(self):
        a = Rational(1, 5)
        b = Rational(2, 5)
        self.assertEqual(str(a.div(b)),"5/10")
        a = Rational(3, 7)
        b = Rational(8, 3)
        self.assertEqual(str(a.div(b)),"9/56")
        a = Rational(3,4)
        b = Rational(-1,4)
        self.assertEqual(str(a.div(b)),"12/-4")

    def test_cmp(self):
        a = Rational(2, 5)
        b = Rational(1, 5)
        self.assertEqual(a.cmp(b),1)
        a = Rational(3, 7)
        b = Rational(8, 3)
        self.assertEqual(a.cmp(b),-1)
        a = Rational(75,125)
        b = Rational(3,5)
        self.assertEqual(a.cmp(b),0)