# Mehdi Najmi- Thursday 14-18
# to calculate factoriel

def factorial(a):
    if a==1:
        print(' factoriel 1 is equal to 1')
    elif a<0:
        print( ' o does not have a factorial')
    else:
        return a*factorial(a-1)

factorial(-1)
