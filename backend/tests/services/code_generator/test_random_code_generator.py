import unittest

from backend.src.services.code_generator import RandomCodeGeneratorService


class TestRandomCodeGeneratorService(unittest.TestCase):
    def setUp(self):
        self.generator = RandomCodeGeneratorService()

    def test_generate_returns_a_string(self):
        self.assertIsInstance(self.generator.generate(length=5), str)

    def test_generate_returns_code_with_specified_length(self):
        length_1 = 10
        length_2 = 255
        code_1 = self.generator.generate(length_1)
        code_2 = self.generator.generate(length_2)
        self.assertTrue(len(code_1) == length_1)
        self.assertTrue(len(code_2) == length_2)

if __name__ == "__main__":
    unittest.main()