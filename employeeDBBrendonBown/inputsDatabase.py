from productClass import Product

def getProduct():

    #Get product information
    print()
    productName = input("Enter Product Name >>> ")
    productNum = input("Enter Product Number >>> ")
    productQuantity = input("Enter Product Quantity >>> ")
    productCost = input("Enter cost of product >>> ")
    print()

    #Create a product and return it
    product = Product(productNum, productName, productQuantity, productCost);
