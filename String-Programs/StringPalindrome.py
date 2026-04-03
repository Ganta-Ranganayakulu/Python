#check if the string is palindrome or not
a=input("Enter a string")
rev=a[::-1]
if (a==rev):
    print("the given string is a palindrome")
else:
    print("not a palindrome")
