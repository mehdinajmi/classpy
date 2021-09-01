# Mehdi Najmi- Thursday 14-18
# BMI calculation  along if conditions
def calcultion_bmi(weight,height):
	bmi=float(weight)/(float(height)**2)
	print(bmi)
	if bmi>=18.5 and bmi<=24.5:
		print (' you are in healthy range')
	elif bmi <18.5:
		print( 'you are underweight')
	else:
		print('you are overweight')
