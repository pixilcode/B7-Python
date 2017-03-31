from modules.inputsDatabase import getProduct
from modules.readWriteFiles import writeProductFile
from modules.calculationModule import calculation
import time

#Number of items to ask for
NUM_OF_ITEMS = 3;

#Variable that holds all products
products = [];

#Loop for the number of items to get the product and calculate stuff
for i in range(NUM_OF_ITEMS):
    product = getProduct();
    product = calculation(product);
    products.append(product);

#Aesthetics
print("Writing to file", end="");
time.sleep(1);
print(".", end="");
time.sleep(1);
print(".", end="");
time.sleep(1);
print(".");
time.sleep(1);

#Write the file
writeProductFile(products);

print("File written successfully!");

