str=input("enter an string:")
if len(str)>1:
    r=str[-1]+str[1:-1]+str[0]
else:
    r = str
print("result",r)