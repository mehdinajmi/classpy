#To sum of numbers between 1 to 1000 the remainings divided by 3 is equal to zero
# Mehdi Najmi- sematec Python class - Thursday 2:00 pm to 6:00 pm
list_adad=[]
list_position=0
adad=0
while adad <=1000:

    if adad %3==0:
        list_adad.append(adad)
    adad+=1
    list_position+=1
print(list_adad)
print('The Total number is:' ,sum(list_adad))
