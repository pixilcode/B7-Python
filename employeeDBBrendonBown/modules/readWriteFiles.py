from employeeClass import Employee

inputExt = "txtFiles/";
outputExt = "output/"

def writeProductFile(products):

    #Open a file to store the data
    file = open((outputExt + "products.txt"), "w");

    #Write the header
    file.write("Name\t\t|" + "Number\t\t|" + "Quantity\t|" + "Cost\t\t|" + "Inventory\t\t|" + "Price\n");
    
    #Loop through each product
    for product in products:
        file.write(product.toString());
        file.write("\n");

    file.close();

def readEmployeeFile():
    empData = open(inputExt + "employee_data.txt", "r");
    laborData = open(inputExt + "labor_data.txt", "r");
    employees = [];

    for line in empData:
        words = line.split(" ");
        tempEmp = Employee(words[0], words[1], words[2]);
        employees.append(tempEmp);

    employee = 0;
    for line in laborData:
        words = line.split(" ");
        employees[employee].setWageAndHours(words[0], words[1]);
        
