# Write your unit tests here!
import unittest
from optimal_change import optimal_change

class TestOptimalChange(unittest.TestCase):
    #test edge and special cases
    def test_exact_pay(self):
        self.assertTrue(optimal_change(51.53, 51.53) == "The optimal change for an item that costs $51.53 with an amount paid of $51.53 is No changes needed!")

    def test_no_enough_pay(self):
        self.assertTrue(optimal_change(9.87, 0) == "The optimal change for an item that costs $9.87 with an amount paid of $0 is Please pay with enough amount!")

    def test_single_domination_1(self):
        self.assertEqual(optimal_change(50, 100), "The optimal change for an item that costs $50 with an amount paid of $100 is 1 $50 bill.")

    def test_multi_domination_1(self):
        self.assertEqual(optimal_change(3, 50), "The optimal change for an item that costs $3 with an amount paid of $50 is 2 $20 bills, 1 $5 bill, 2 $1 bills.")

    #some normal cases with penny
    def test_normal_cases_1(self):
        self.assertEqual(optimal_change(62.13, 100), "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

    def test_normal_cases_2(self):
        self.assertEqual(optimal_change(31.51, 50), "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

    def test_normal_cases_3(self):
        self.assertEqual(optimal_change(0.01, 99), "The optimal change for an item that costs $0.01 with an amount paid of $99 is 1 $50 bill, 2 $20 bills, 1 $5 bill, 3 $1 bills, 3 quarters, 2 dimes, and 4 pennies.") 
              
if __name__ == '__main__':
    unittest.main()