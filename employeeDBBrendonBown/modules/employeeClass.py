class Employee:

    def __init__(this, ID, first, last):
        this.first = first[0:(len(first) - 2)];
        this.last = last;
        this.id = ID;
        this.wage = 0;
        this.hours = 0;
        this.grossWage = 0;
        this.taxes = 0;
        this.netPay = 0;

    def setWageAndHours(this, wage, hours):
        this.wage = wage;
        this.hours = hours;
    
    def setGrossWage(this, grossWage):
        this.grossWage = grossWage;

    def setTaxes(this, taxes):
        this.taxes = taxes;

    def setNetPay(this, netPay):
        this.netPay = netPay;

    def toString(this):
        string = str(this.last) + str(this.first) + "\t" + str(this.id) + "\t" + str(this.wage) + "\t" + str(this.hours) + "\t" + str(this.grossWage) + "\t" + str(this.taxes) + "\t" + str(this.netPay);
        return string;

    def addTabs(this, string):
        if len(string) > 8:
            return string + "\t";
        elif len(string) > 4:
            return string + "\t\t";
        else:
            return string + "\t\t\t";
        
