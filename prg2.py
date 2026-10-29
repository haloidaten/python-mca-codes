str=input("enter string")
F_c=str[0]
r=F_c+str[1:].replace(F_c,'$')
print("result",r)