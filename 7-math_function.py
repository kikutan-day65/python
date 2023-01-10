#some functions are in math module, so it's required to import it.
import math

pi = 3.14
num = -100

x, y, z = 1, 2, 3

# round() = output should be 3
print(round(pi))


# ceil() = output should be 4
print(math.ceil(pi))


# floor() = output should be 3
print(math.floor(pi))


# abs() = returns absolute value. output should be 100
print(abs(num))


# pow(A, B) = output should be A powered B
print(pow(pi, 2))


# sqrt() = output should be square root of 49
print(math.sqrt(49))


# max() = returns the maximum value
max = max(x, y, z)
print("max value is : " + str(max))


# min() = returns the minimum value 
min = min(x, y, z)
print("min value is : " + str(min))