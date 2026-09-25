# LABWORK 1
print("LABWORK 1:")
# EXERCISE 1:
print("EX1:")
r = float(input("Enter circle radius? "))
print("Circle area =", r*r*3.14)

# EXERCISE 2:
print("EX2:")
t = float(input("Enter the temperature in Celsius? "))
print(t, "(C) =", t*1.8 +32, "(F)")

# EXERCISE 3:
print("EX3:")

n = int(input("Enter a number? "))
if n < 2:
    print(n, "is a NOT prime number")
else: 
    for i in range(2, n):
        if n % i == 0:
            print(n, "is a NOT prime number")
            break
        else: 
            print(n, "is a prime number")
            break

# EXERCISE 4:
print("EX4:")

m = int(input("Enter a number? "))
sum = 0
for i in range(1,m):
    if n % i == 0:
        sum = sum + i
if sum == m:
    print(m, "is a perfect number")
else:
    print(m, "is NOT a perfect number")

# EXERCISE 5:
print("EX5:")

colors = ["red", "blue", "black", "white", "green", "silver"]
color = input("What is your favorite color? ")
if color in colors:
    print("Your coulor is at index ", colors.index(color),"in my list")
else: 
    print("Sorry, I could not find your color")

# EXERCISE 6:
print("EX6:")

print("range1:", end = " ")
for i in range(7):
    if i !=6:
        print(i, end = ", ")
    else:
        print(i)
print("range2:", end =" ")
for i in range(1, 11, 3):
    if i !=10:
        print(i, end = ", ")
    else: 
        print(i)

print("range3:", end = " ")
for i in range (5, 0, -1):
    if i !=1:
        print(i, end = ", ")
    else: 
        print(i)
print("range4:", end = " ")
for i in range(6, -3, -2):
    if i != -2: 
        print(i , end = ", ")
    else: 
        print(i)

# EXERCISE 7:
print("EX7:")

def remove_dollar_sign(s):
    return s.replace ("$", "")
s = input("Enter a string: ")
print(remove_dollar_sign(s))

# EXERCISE 8:
print("EX8:")

def extract_even(l):
    result = []
    for i in l:
        if i % 2 == 0:
            result.append(i)
    return result

numbers = [1, 4, 5, -1, 10]
print(extract_even(numbers))

# EXERCISE 9:
print("EX9:")

v = int(input("Enter a non-negetive integer: "))
def factorial(v):
    result = 1
    for i in range(1, v + 1):
        result = result * i 
    return result
print("Factorial of", v, "is", factorial(v))

# EXERCISE 10: 
print("EX10:")

def get_divisors(o):
    for i in range(1, o + 1):
        if n % i == 0:
            print(i)
n= int(input("Enter a number: "))
get_divisors(n)

# EXERCISE 11: 
print("EX11:")

import math
x1, y1 = map(int, input(). split())
x2, y2 = map(int, input().split())
a = (x2 - x1 ); b = (y2 - y1)
d = math.sqrt(a ** 2 + b ** 2)
print("Distance between two points:", round(d, 2))

# EXERCISE 12:
print("EX12:")

q,p = map(int, input().split())
for i in range(p):
    print("*", end= " ")
print(" ")
for i in range( q-2):
    for j in range(p):
        if (j == 0 or j == p-1):
            print("*", end= " ")
        else:
            print(end = "  ")
    print("")
for i in range(p):
    print("*", end= " ")

