a=input("Enter a string")
vowels="aeiouAEIOU"
vowelcount=0
for i in a:
    for j in vowels:
        if i==j:
             vowelcount=vowelcount+1     
print(vowelcount)
print(len(a))

#or
a=input("Enter a string")
vowels="aeiouAEIOU"
vowelcount=0
for i in a:
    if i in vowels:
        vowelcount=vowelcount+1
print(vowelcount)
print(len(a))
