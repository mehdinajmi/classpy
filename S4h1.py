### to work out  BMI result
### Mehdi Najmi- sematec Python class - Thursday 2:00 pm to 6:00 pm
def calcultion_bmi(height,weight):
	bmi=float(weight)/(float(height)**2)
	return bmi
def bmi_result(height,weight):
	if calcultion_bmi(height,weight) >25:
		print (' you are over weight')
	elif calcultion_bmi(height,weight) <18:
		print(' you are under weight')
	else:
		print(' you are in healthy range')
bmi_result(1.65,75)
this line is added on 19/08/2024 at 10:48 pm
