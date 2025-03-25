#arithmetic operators
a = 5
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #reminder
print(a ** b) 

#relational operators( Always Return Boolean Value {True/Flase})
#when we compare any two numbers
a = 50
b = 20

print(a == b) #false
print(a != b) #false

#assignment operators
num = 5
num *= 5
print(num)
num /= 5
print("num: ", num)

#Logical Operators
#It alwasys works with boolean value

print(not False) #True
print(not True) #False

#we also use like this
a = 3
b = 5
print(not False)
print(not (a > b)) #The correct answer is false,,, because we use not operator therefore is shows True
print(not(a==b)) #The correct answer is false,, therefore is shows True

#and operator
val1 = True
val2 = True
print("And operator is:", val1 and val2)
