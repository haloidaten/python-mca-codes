num = [-5, 10, -3, 7, 0, 8, -2]
pos = [x for x in num if x > 0]
print('positive', pos)


n= int(input("enter the value of n"))
num=[int(input("enter the number:")) for i in range(n)]
s=[x**2 for x in num]
print("squre",s)

w=input("enter a word")
v=[ch for ch in w if ch in 'aeiouAEIOU' ]
print("vowels:",v)

v=input("enter a word")
ov=[ord(ch) for ch in v]
print("ordinal values:",ov)

