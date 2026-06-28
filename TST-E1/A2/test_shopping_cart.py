import unittest
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    # Läuft vor jedem einzelnen Test und erstellt einen frischen Warenkorb
    def setUp(self):
        self.cart = ShoppingCart()

    def test_new_cart_is_empty(self):
        self.assertEqual(self.cart.get_count(), 0)

    def test_add_product_increases_count(self):
        self.cart.add_product("Apfel")
        self.assertEqual(self.cart.get_count(), 1)

if __name__ == '__main__':
    unittest.main()