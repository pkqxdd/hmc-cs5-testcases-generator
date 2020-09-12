# CS5 Test Case Generator

Getting tired of having to copy and paste every single example into your code just to figure out if your code works? With this program, it won't be a problem anymore! It can create test cases from the problem description like never before!

## Dependencies installation

Before running the program, you must install the required dependencies first by running

```sh
python3 -m pip install requests, bs4
```

## Test case generation

Simply run the program (`python3 hw_parser.py`) and provides it with the URL to the problem when prompted. Example output created by the program (file content in `hw2pr4_test.py`, created by running the program on https://www.cs.hmc.edu/twiki/bin/view/CS5/BlackRNANew)

```py
import unittest
from hw2pr4 import *


class Part1rnafolding(unittest.TestCase):
    def test_test26(self):
        try:
            self.assertEqual(fold("ACCCCCU"), 1)
            self.assertEqual(fold("ACCCCGU"), 2)
            self.assertEqual(fold("AAUUGCGC"), 4)
            self.assertEqual(fold("ACUGAGCCCU"), 3)
            self.assertEqual(fold("ACUGAGCCCUGUUAGCUAA")  , 8)
        except NameError:
            self.skipTest("Not implemented")



class Optionalbonusparta10points(unittest.TestCase):
    def test_test3(self):
        try:
            myList = [[42, ["foo", "bar", "spam"]], [32, ["hi", "mom"]], [24, ["this", "is", "weird"]]]
            self.assertEqual(max(myList), [42, ['foo', 'bar', 'spam']])
            self.assertEqual(min(myList), [24, ['this', 'is', 'weird']])
        except NameError:
            self.skipTest("Not implemented")

    def test_test7(self):
        try:
            self.assertEqual(getFold("ACCCCCU"), [1, [[0, 6]]])
            self.assertEqual(getFold("ACCCCGU"), [2, [[0, 6], [4, 5]]])
            self.assertEqual(getFold("AAUUGCGC"), [4, [[0, 3], [1, 2], [4, 5], [6, 7]]])
            self.assertEqual(getFold("ACUGAGCCCU"), [3, [[1, 3], [4, 9], [5, 6]]])
            self.assertEqual(getFold("ACUGAGCCCUGUUAGCUAA")  , [8, [[0, 2], [3, 7], [5, 6], [8, 10], [11, 18], [12, 13], [14, 15], [16, 17]]])
        except NameError:
            self.skipTest("Not implemented")


if __name__ == '__main__':
    unittest.main()
```

To run the test, simply run the generated test file. If it shows OK with no test skipped, then you are golden!
