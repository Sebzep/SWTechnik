import unittest
from unittest.mock import patch
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    
    def setUp(self):
        self.cart = ShoppingCart()

    # Test 1
    def test_new_cart_is_empty(self):
        self.assertEqual(self.cart.get_count(), 0)

    # Test 2
    def test_add_product_increases_count(self):
        self.cart.add_product("Apfel")
        self.assertEqual(self.cart.get_count(), 1)

    # Test 3 (Prüf hier mal das "test_" am Anfang)
    @patch('shopping_cart.Database.get_price_from_db')
    def test_get_total_price_with_mock(self, mock_get_price):
        mock_get_price.side_effect = [1.50, 2.00]
        self.cart.add_product("Apfel")
        self.cart.add_product("Birne")
        self.assertEqual(self.cart.get_total_price(), 3.50)
        self.assertEqual(mock_get_price.call_count, 2)

if __name__ == '__main__':
    unittest.main()