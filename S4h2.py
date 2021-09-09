### to do  calculation of math_geometric
### Mehdi Najmi- sematec Python class - Thursday 2:00 pm to 6:00 pm
def calculation_math_geometric(length:int,width:int,height:int):
   type=input('enter a math geometric name:\n')
   dimension=input('enter a math geometric name:\n')
   if type.lower()== 'cubiod' and dimension.lower()=='volume':
      return length*width*height
   elif  type.lower()== 'cubiod' and dimension.lower()=='area':
      return (2*width*height)+(2*length*height)+(2*length*width)
   elif  type.lower()== 'cube' and dimension.lower()=='volume':
      return length*width*height
   elif  type.lower()== 'cube' and dimension.lower()=='area':
       return 6*length*width
   else:
      print (' there is not enough information to do calculation')

print(calculation_math_geometric(3,3,3))
