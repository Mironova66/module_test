import unittest
import module2

class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(module2.module2(3111), "Input Error")
    def test2(self):
        self.assertEqual(module2.module2(713524), True)

class Test2(unittest.TestCase):
    def test1(self):
        self.assertEqual(module2.module2(101235), False)
    def test2(self):
        self.assertEqual(module2.module2(456), "Input Error")

class Test3(unittest.TestCase):
    def test1(self):
        self.assertEqual(module2.module2(123456), False)
    def test2(self):
        self.assertEqual(module2.module2("vgrer4w4"), "Input Error")

class Test4(unittest.TestCase):
    def test1(self):
        self.assertEqual(module2.module2(185536), True)
    def test2(self):
        self.assertEqual(module2.module2("/////////"), "Input Error")

if __name__ == "__main__":
  unittest.main()
