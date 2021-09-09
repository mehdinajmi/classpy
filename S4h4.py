### to do math calculation on shapes
### Mehdi Najmi- sematec Python class - Thursday 2:00 pm to 6:00 pm 

def calculation(shape, request):
	""" this is the function to calculate
diemnctions """

	if shape=='rectangle'and request=='area':
		tool=int(input('enter tool:\n'))
		arz=int(input('enter arz:\n'))
		return tool*arz
	elif shape=='rectangle'and request=='space':
		tool=int(input('enter tool:\n'))
		arz=int(input('enter arz:\n'))
		return (tool+arz)*2
	elif shape=='square'and request=='area':
		tool=int(input('enter tool:\n'))
		arz=int(input('enter arz:\n'))
		return tool*2
	elif shape=='square'and request=='space':
		tool=int(input('enter tool:\n'))
		arz=int(input('enter arz:\n'))
		return tool*4
	else:
		print (' i can not calculate due to not giving rnogth information')
