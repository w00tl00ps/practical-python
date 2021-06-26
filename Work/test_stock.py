# test_stock.py

import stock
import unittest

unittest.TestCase

class TestStock(unittest.TestCase):
    def test_create(self):
        ''' Test instance creation'''
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        ''' Test the cost property of the class'''
        s = stock.Stock('GOOG', 100, 490.1)    
        self.assertEqual(s.cost, 49010.0)

    def test_sell(self):
        ''' Test the sell function'''
        s = stock.Stock('GOOG', 100, 490.1)
        s.sell(50)
        self.assertEqual(s.shares, 50)

    def test_bad_shares(self):
        ''' Test that shares can't be a non-integer value'''
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = '100'

        
# Main class to run the tests
if __name__ == '__main__':
    unittest.main()