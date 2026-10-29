t=input("enter a string")
f={}
for ch in t:
    if ch in f:
        f[ch]=f[ch]+1
    else:
        f[ch]=1
    print(f)