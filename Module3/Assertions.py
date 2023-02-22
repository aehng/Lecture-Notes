import unittest


# This program demonstrates how to use the various assertions provided by the
# unittest library


class UnitTestTester(unittest.TestCase):
    def test_Equal(self):
        a = 'A string'
        b = 'A string'
        self.assertEqual(a, b)
        
        a = 1
        b = 1
        self.assertEqual(a, b)
        
        # In Python floating-point numbers are indistinguishable after 17
        # decimal places
        a = 1.00000000000000001
        b = 1.00000000000000002
        self.assertEqual(a, b)


    def test_NotEqual(self):
        a = 'A string'
        b = 'Another string'
        self.assertNotEqual(a, b)
        
        a = 1
        b = 2
        self.assertNotEqual(a, b)
        
        # In Python these floating-point numbers differ in the 16th decimal
        # place, and are distinct
        a = 1.0000000000000001
        b = 1.0000000000000002
        self.assertNotEqual(a, b)


    def test_AlmostEqual(self):
        a = 3.141592653589793
        b = 102928 / 32763
        self.assertAlmostEqual(a, b)


    def test_Greater(self):
        a = 3.141592653589793
        b = 223/71
        self.assertGreater(a, b)


    def test_Less(self):
        a = 3.141592653589793
        b = 22/7
        self.assertLess(a, b)



    def test_True(self):
        a = True
        self.assertTrue(a)
        
        # Certain Python values can be converted to Boolean true:
        a = 1
        self.assertTrue(a)
        a = -1
        self.assertTrue(a)
        a = "true"
        self.assertTrue(a)
        a = {'this dictionary': 'is not empty'}
        self.assertTrue(a)


    def test_False(self):
        a = False
        self.assertFalse(a)
        
        # As above, certain Python values can be converted to Boolean false:
        a = 0
        self.assertFalse(a)
        a = ""
        self.assertFalse(a)
        a = {}
        self.assertFalse(a)


    def test_Is(self):
        a = list(range(30))
        b = a
        self.assertIs(a, b)


    def test_IsNot(self):
        a = list(range(30))
        b = list(range(30))
        self.assertEqual(a, b)
        self.assertIsNot(a, b)


    def test_IsNone(self):
        a = None
        self.assertIsNone(a)


    def test_IsNotNone(self):
        a = False
        self.assertIsNotNone(a)


    def test_In(self):
        needle = 'needle'
        haystack = [ "planetesimal", "cleared", "realizations", needle,
                "ballad", "pessimist", ]
        self.assertIn(needle, haystack)


    def test_NotIn(self):
        needle = 'needle'
        haystack = [ "planetesimal", "cleared", "realizations",
                "ballad", "pessimist", ]
        self.assertNotIn(needle, haystack)


    def test_CountEqual(self):
        a = list(range(30))
        b = tuple(range(30))
        self.assertCountEqual(a, b)


if __name__ == '__main__':
    unittest.main()
