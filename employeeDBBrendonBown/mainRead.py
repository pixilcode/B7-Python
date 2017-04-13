from modules.calculationModule import calcEmployeeData
from modules.readWriteFiles import readEmployeeFile
from modules.user import outputEmployeeData

employees = readEmployeeFile();
for i in range(len(employees)):
    employees[i] = calcEmployeeData(employees[i]);
    
outputEmployeeData(employees);
