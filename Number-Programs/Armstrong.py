a=int(input("Enter a Number"))
number=a
rev=0
while(a>0):
    d=a%10
    rev=rev+d*d*d
    a=a//10
if(number == rev):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
