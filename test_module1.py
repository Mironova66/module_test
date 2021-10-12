import unittest
import module1

class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(module1.module1(156), True)
    def test2(self):
        self.assertEqual(module1.module1(34), True)

class Test2(unittest.TestCase):
    def test1(self):
        self.assertEqual(module1.module1(1), False)
    def test2(self):
        self.assertEqual(module1.module1("vgrvd"), "Input Error")

class Test3(unittest.TestCase):
    def test1(self):
        self.assertEqual(module1.module1("ккккк"), "Input Error")
    def test2(self):
        self.assertEqual(module1.module1(4444444447), False)

class Test4(unittest.TestCase):
    def test1(self):
        self.assertEqual(module1.module1("..не62"), "Input Error")
    def test2(self):
        self.assertEqual(module1.module1(-98), True)

if __name__ == "__main__":
  unittest.main()
