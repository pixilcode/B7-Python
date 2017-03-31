def calculation(enter): #uses the inputs from the user-input
    enter.setProductPrice(float(enter.cost) * 1.35)
    enter.setInventoryCost(float(enter.cost) * float(enter.quantity))
    return enter
