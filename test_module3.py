import unittest
import module3

class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(module3.module3(3111), 6)
    def test2(self):
        self.assertEqual(module3.module3(16), 7)

class Test2(unittest.TestCase):
    def test1(self):
        self.assertEqual(module3.module3(-101235), 12)
    def test2(self):
        self.assertEqual(module3.module3(456), 15)

class Test3(unittest.TestCase):
    def test1(self):
        self.assertEqual(module3.module3(-123456), 21)
    def test2(self):
        self.assertEqual(module3.module3("4vfdf"), "Input Error")

class Test4(unittest.TestCase):
    def test1(self):
        self.assertEqual(module3.module3(1), 1)
    def test2(self):
        self.assertEqual(module3.module3("----"), "Input Error")

if __name__ == "__main__":
  unittest.main()
