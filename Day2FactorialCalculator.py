import math

def factorialCalculator():
    while True:
        number=int(input("Enter a number: "))
        finalFactorial=1
        while number>0:
            finalFactorial=finalFactorial*number
            number-=1
        print(finalFactorial)
factorialCalculator()