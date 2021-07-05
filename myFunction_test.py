import unittest
from myFunction import myFunction

class TestMyFunction(unittest.TestCase):

    def test_myFunction(self):
        firstArg = 1
        secondArg = 2
        result = 3
        self.assertEqual(myFunction(firstArg , secondArg), result)

if __name__ == '__main__':
    unittest.main()