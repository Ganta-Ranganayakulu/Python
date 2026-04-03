a=int(input("Enter a number"))
number=a
rev=0
while(a>0):
    d=a%10
    rev=(rev*10)+d
    a=a//10
if(rev==number):
    print(rev)
    print("palindrome")
else:
    print(rev)
    print("not a palindrome")
