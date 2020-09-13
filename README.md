# CS5 Test Case Generator

Getting tired of having to copy and paste every single example into your code just to figure out if your code works? With this program, it won't be a problem anymore! It can create test cases from the problem description like never before!

## Dependencies installation

Before running the program, you must install the required dependencies first by running

```sh
python3 -m pip install requests, bs4
```

## Running the program

To run the program, you can simply clone this repository and run `parser.py`

```bash
git clone https://github.com/pkqxdd/hmc-cs5-testcases-generator
cd hmc-cs5-testcases-generator
python3 parser.py
```

The program will prompt you for the link of the web page, just copy and paste the link into your terminal.

If you don't want to be prompted, you can also give the link as the first positional argument, like this

```bash
python3 parser.py https://www.cs.hmc.edu/twiki/bin/view/CS5/BlackRNANew
```

## Use the generated test cases

Disclaimer: the test cases are fetched and extracted from the website you gave. It is not guaranteed to be 
complete nor correct. It fetches the expected input/output verbatim as the website. In case there is a typo  
on the website, the generated script may contain syntax errors and/or is otherwise erroneous. 

To run the test cases, you can simply run the generated Python file, such as

``` 
python3 hw2pr4_test.py
```

Your solution (in this case `hw2pr4.py`) must be present either in the current working directory OR
in the same directory as the test script. 

Note that you don't need to understand the generated program to use it. So long as it shows OK with no test skipped, 
you are golden!

## Example of generated test cases

This section is intended for people who are curious what's going on without having to run the script.
If you have no idea what's inside, it's totally OK!

```
$ python3 parser.py https://www.cs.hmc.edu/twiki/bin/view/CS5/BlackRNANew

Sending HTTP request...
Parsing response HTML...
Parsing expected input/output for homework 2 problem 4...

Parsing test cases for p0

Parsing test cases for  Part 1:  RNA Folding... 
Test case 0 expected input: fold("ACCCCCU")
Test case 0 expected output: 1

Test case 1 expected input: fold("ACCCCGU")
Test case 1 expected output: 2

Test case 2 expected input: fold("AAUUGCGC")
Test case 2 expected output: 4

Test case 3 expected input: fold("ACUGAGCCCU")
Test case 3 expected output: 3

Test case 4 expected input: fold("ACUGAGCCCUGUUAGCUAA")  
Test case 4 expected output: 8


Parsing test cases for  Optional Bonus Part A (10 Points) 
Test case 0 expected input: myList = [[42, ["foo", "bar", "spam"]], [32, ["hi", "mom"]], [24, ["this", "is", "weird"]]]
Test case 0 expected input: max(myList)
Test case 0 expected output: [42, ['foo', 'bar', 'spam']]

Test case 1 expected input: min(myList)
Test case 1 expected output: [24, ['this', 'is', 'weird']]

Test case 0 expected input: getFold("ACCCCCU")
Test case 0 expected output: [1, [[0, 6]]]

Test case 1 expected input: getFold("ACCCCGU")
Test case 1 expected output: [2, [[0, 6], [4, 5]]]

Test case 2 expected input: getFold("AAUUGCGC")
Test case 2 expected output: [4, [[0, 3], [1, 2], [4, 5], [6, 7]]]

Test case 3 expected input: getFold("ACUGAGCCCU")
Test case 3 expected output: [3, [[1, 3], [4, 9], [5, 6]]]

Test case 4 expected input: getFold("ACUGAGCCCUGUUAGCUAA")  
Test case 4 expected output: [8, [[0, 2], [3, 7], [5, 6], [8, 10], [11, 18], [12, 13], [14, 15], [16, 17]]]


Parsing test cases for  Optional Bonus Part B (10 Points) 

Parsing test cases for  Submit 
Writing assertions to hw2pr4_test.py...
File wrote to /Users/jerie/Desktop/hmc-cs5-testcases-generator/hw2pr4_test.py
```

Example of generated file (`hw2pr4_test.py`)

```py
import unittest, sys, os
sys.path.append(os.path.abspath(os.getcwd()))

try:
    from hw2pr4 import *
except ImportError:
    print("Unable to find hw2pr4.py. Please make sure it is either in the current working directory"
          "or is in the same directory as this script.", file=sys.stdout, flush=True)
    sys.exit(1)


class Part1rnafolding(unittest.TestCase):
    def test_test26(self):
        try:
            self.assertEqual(fold("ACCCCCU"), 1)
            self.assertEqual(fold("ACCCCGU"), 2)
            self.assertEqual(fold("AAUUGCGC"), 4)
            self.assertEqual(fold("ACUGAGCCCU"), 3)
            self.assertEqual(fold("ACUGAGCCCUGUUAGCUAA")  , 8)
        except NameError as e:
            self.skipTest(e.args[0])



class Optionalbonusparta10points(unittest.TestCase):
    def test_test3(self):
        try:
            myList = [[42, ["foo", "bar", "spam"]], [32, ["hi", "mom"]], [24, ["this", "is", "weird"]]]
            self.assertEqual(max(myList), [42, ['foo', 'bar', 'spam']])
            self.assertEqual(min(myList), [24, ['this', 'is', 'weird']])
        except NameError as e:
            self.skipTest(e.args[0])

    def test_test7(self):
        try:
            self.assertEqual(getFold("ACCCCCU"), [1, [[0, 6]]])
            self.assertEqual(getFold("ACCCCGU"), [2, [[0, 6], [4, 5]]])
            self.assertEqual(getFold("AAUUGCGC"), [4, [[0, 3], [1, 2], [4, 5], [6, 7]]])
            self.assertEqual(getFold("ACUGAGCCCU"), [3, [[1, 3], [4, 9], [5, 6]]])
            self.assertEqual(getFold("ACUGAGCCCUGUUAGCUAA")  , [8, [[0, 2], [3, 7], [5, 6], [8, 10], [11, 18], [12, 13], [14, 15], [16, 17]]])
        except NameError as e:
            self.skipTest(e.args[0])


if __name__ == '__main__':
    unittest.main(verbosity=2)
```

## License

MIT License

Copyright (c) 2020 Jerie Wang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
