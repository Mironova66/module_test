import unittest
import module4

class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(module4.module4(16, '+'), '++++++\n+ 16 +\n++++++')
    def test2(self):
        self.assertEqual(module4.module4("vgrve", '+'), "Input Error")

class Test2(unittest.TestCase):
    def test1(self):
        self.assertEqual(module4.module4(1234567, '-'), '-----------\n- 1234567 -\n-----------')
    def test2(self):
        self.assertEqual(module4.module4("...........", '+'), "Input Error")

class Test3(unittest.TestCase):
    def test1(self):
        self.assertEqual(module4.module4(-89, '/'), '///////\n/ -89 /\n///////')
    def test2(self):
        self.assertEqual(module4.module4("fff44", '.'), "Input Error")

class Test4(unittest.TestCase):
    def test1(self):
        self.assertEqual(module4.module4(-56, '/'), '///////\n/ -56 /\n///////')
    def test2(self):
        self.assertEqual(module4.module4("56ggd", '+'), "Input Error")

if __name__ == "__main__":
  unittest.main()
