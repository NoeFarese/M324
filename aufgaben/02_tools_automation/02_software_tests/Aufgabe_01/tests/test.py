import unittest
import os
from src.File import File

class TestFile(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_temp.txt"
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass

    def test_create_file(self):
        File.create_file(self.test_file)
        self.assertTrue(os.path.exists(self.test_file))
        self.assertEqual(os.path.getsize(self.test_file), 0)

    def test_write_to_file(self):
        File.write_to_file(self.test_file, "Hello World")
        with open(self.test_file, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertEqual(content, "Hello World")

    def test_read_from_file(self):
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write("Sample Text")
        content = File.read_from_file(self.test_file)
        self.assertEqual(content, "Sample Text")


if __name__ == "__main__":
    unittest.main()
