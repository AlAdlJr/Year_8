# Doing mathematics - I.Aladl - 1.1

import math , random

print('Input number to approximate')
num1 =float(input())
print(' Rounded Up:' , math.ceil(num1))
print(' Rounded Down:' , math.floor(num1))

print('Input number to be squared and to find the square root')
num2 = int (input())
print(num2 , 'Squared:' , math.pow( num2 , 2))
print(num2 , 'Square Root:' , math.sqrt(num2))

nums = random.sample(range( 1, 49) , 6)

print( 'Your Lucky Lotto Numbers Are:' , nums)
