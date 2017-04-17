def findMax(list):
	if len(list) == 1:
		return list[0];
	else:
		num1 = findMax(list[1:]);
		num2 = list[0];
		if num1 > num2:
			return num1;
		else:
			return num2;

print(findMax([347, 425, 864, 123]));
