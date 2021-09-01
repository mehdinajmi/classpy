# Mehdi Najmi- Thursday 14-18
# mathematic calculation based on given operation sign
def math_operation(firstnumber,secondnumber,mathsymbol):
	print(f' two numbers entered are: {firstnumber} and {secondnumber}')
	if mathsymbol=='+':
		print('result is equal to :',firstnumber+secondnumber)
	elif mathsymbol=='-':
		print('result is equal to :',firstnumber-secondnumber)
	elif mathsymbol=='*':
		print('result is equal to :',firstnumber*secondnumber)
	else:
		print('result is equal to :',firstnumber/secondnumber)
