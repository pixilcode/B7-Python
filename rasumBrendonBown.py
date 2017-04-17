def sum(list):
	if len(list) == 1:
		return list[0];
	else:
		return list[0] + sum(list[1:]);

print(sum(range(10)));
