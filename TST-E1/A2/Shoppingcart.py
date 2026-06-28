class ShoppingCart:
    def __init__(self):
        # Wir erstellen eine Liste für die Produkte
        self.items = []

    def add_product(self, product):
        # Produkt in die Liste packen
        self.items.append(product)

    def get_count(self):
        # Jetzt geben wir die echte Länge der Liste zurück
        return len(self.items)