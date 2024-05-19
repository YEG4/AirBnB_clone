"""Tests use cases  for the class BaseModel
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """This class is used to test BaseModel class
    """
    def setUp(self):
        """setUp method that runs before every test
        """
        pass

    def test_add(self):
        """A TestComment
        """
        self.assertEqual(10, 10)


if __name__ == "__main__":
    unittest.main()
