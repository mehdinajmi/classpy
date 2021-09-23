# To careat a list within a function
# Mehdi Najmi- sematec Python class - Thursday 2:00 pm to 6:00 pm
def get_list():
	list1=[]
	while len(list1)<=10:
		number=int(input('enter a number:\n'))
		list1.append(number)
	print(list1)
