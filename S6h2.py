# to calculate the average of a list
### Mehdi Najmi- sematec Python class - Thursday 2:00 pm to 6:00 pm
list=[]
while len(list) <=10:
    number=int(input('Enter a Number:\n'))
    list.append(number)
print('The average is equal to',sum(list)/len(list))
