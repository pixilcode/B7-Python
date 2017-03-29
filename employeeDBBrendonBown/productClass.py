class Product:

    def __init__(this, number, name, quantity, cost):
        this.number = number;
        this.name = name;
        this.quantity = quantity;
        this.cost = cost;

    def setInventoryCost(this, inventoryCost):
        this.inventoryCost = inventoryCost;

    def setProductPrice(this, price):
        this.productPrice = price;

    def toString(this):
        string = str(this.name) + "\t\t|" + str(this.number) + "\t\t|" + str(this.quantity) + "\t\t|" + str(this.cost) + "\t\t|" + str(this.inventoryCost) + "\t\t\t|" + str(this.productPrice);
        return string;
