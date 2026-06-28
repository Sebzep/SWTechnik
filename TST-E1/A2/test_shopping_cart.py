import unittest
# Wir versuchen, eine Klasse zu importieren, die es noch nicht gibt
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def test_new_cart_is_empty(self):
        cart = ShoppingCart()
        # Der Warenkorb sollte am Anfang 0 Produkte enthalten
        self.assertEqual(cart.get_count(), 0)

if __name__ == '__main__':
    unittest.main()