class Database:
    @staticmethod
    def get_price_from_db(product_name):
        # Bleibt leer, da wir es im Test mocken
        pass 

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def get_count(self):
        return len(self.items)

    def get_total_price(self):
        total = 0
        for item in self.items:
            # Hier greift der Code auf die Database-Klasse von oben zu
            total += Database.get_price_from_db(item)
        return total