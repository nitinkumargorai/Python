list = [1, 2, 1]
copy = list.copy()
list.reverse()

if(copy == list):
    print("Palindrome")
else:
    print("Not a Palindrome")

print(copy)