"""Tests use cases  for the class BaseModel
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        pass

    def test_add(self):
        self.assertEqual(10, 10)


if __name__ == "__main__":
    unittest.main()
