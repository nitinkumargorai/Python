#It means when a type of variable will try to change another types of variable, like integer to a floating value
#there are two types of conversion
#1. Conversion (Automatically,,, means no need to take any extra step for doing this, the compiler would automatically done it )
#2. Casting(Manually,,, Means We have to do this)

#Type Conversion
a = 5 #Int Value
b = 1.25 #Float Value
sum = a + b 
print(sum)

print(type(sum))

#Casting
a = int("2")
b = 4.25
print(a + b)

