def writeProductFile(products):

    #Open a file to store the data
    file = open("products.txt", "w");

    #Write the header
    file.write("Name\t|" + "Number\t|" + "Quantity\t|" + "Cost\t|" + "Inventory\t|" + "Price");
    
    #Loop through each product
    for product in products:
        file.write(product.toString());
        file.write("\n");

    file.close();
