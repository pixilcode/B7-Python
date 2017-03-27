class Product:

    def __init__(self, number, name, quantity, cost):
        self.number = number;
        self.name = name;
        self.quantity = quantity;
        self.cost = cost;

    def setInventoryCost(self, inventoryCost):
        self.inventoryCost = inventoryCost;

    def setProductPrice(self, price):
        self.productPrice = price;
