a = int(input("Enter The First Number: "))
b = int(input("Enter The Second Number: "))
c = int(input("Enter The Third Number: "))

if(a >= b  and a >= c ):
    print("The largest Number is", a)
elif(b>=c):
    print("The largest Number is", b)
else:
    print("The largest Number is ", c)