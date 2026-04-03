a=input("Enter a String")
#b=set(a)
#a=str(b)
#print(a)

result = ""

for ch in a:
    if ch not in result:
        result += ch

print(result)
