import unittest
# Wir importieren die Klasse aus der anderen Datei
from Shoppingcart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    
    # Das hier läuft automatisch VOR jedem einzelnen Test
    # So starten wir immer mit einem frischen, leeren Warenkorb
    def setUp(self):
        self.cart = ShoppingCart()

    # Test für Feature 1: Der leere Warenkorb
    def test_new_cart_is_empty(self):
        self.assertEqual(self.cart.get_count(), 0)

    # Test für Feature 2: Produkt hinzufügen
    def test_add_product_increases_count(self):
        self.cart.add_product("Apfel")
        self.assertEqual(self.cart.get_count(), 1)

if __name__ == '__main__':
    unittest.main()