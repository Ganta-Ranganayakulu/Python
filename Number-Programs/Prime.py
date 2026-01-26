a=int(input("Enter a Number"))
count=0
for i in range(2,a+1):
    if a%i==0:
        count+=1
if(count==1):
    print(f"Yes,The given number {a} is a prime")
else:
    print(f"No,The given number {a} is not a prime")
