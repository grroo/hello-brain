import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tiny  # noqa: E402


class TestVersion(unittest.TestCase):
    def test_prints_version(self):
        self.assertEqual(tiny.run(["version"]), f"tiny {tiny.VERSION}")


class TestHello(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(tiny.run(["hello"]), "Hello, world!")

    def test_name_greeting(self):
        self.assertEqual(tiny.run(["hello", "Ada"]), "Hello, Ada!")

    def test_name_with_spaces(self):
        self.assertEqual(tiny.run(["hello", "Ada Lovelace"]), "Hello, Ada Lovelace!")


class TestShout(unittest.TestCase):
    def test_uppercases_one_word(self):
        self.assertEqual(tiny.run(["shout", "hi"]), "HI!")

    def test_joins_words(self):
        self.assertEqual(tiny.run(["shout", "hi", "there"]), "HI THERE!")

    def test_requires_a_word(self):
        with self.assertRaises(SystemExit):
            tiny.run(["shout"])


if __name__ == "__main__":
    unittest.main()
