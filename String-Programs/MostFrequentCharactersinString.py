a=input("Enter the string")
maxcount=0
maxchar=""
for i in a:
    if a.count(i)>maxcount:
        maxcount=a.count(i)
        maxchar=i
print(maxchar)
#or
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if a[i]==a[j]:
            count=count+1
    if count>maxcount:
        maxcount=count
        maxchar=maxchar+a[i]

print(maxcount)
        
