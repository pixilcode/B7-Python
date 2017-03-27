def writeProductFile(products):

    #Open a file to store the data
    file = open("products.txt", "w");

    #Loop through each product
    for i in range(len(products)):
        file.write(products[i].toString());
        file.write("\n");

    file.close();
