a=float(input("enter the first no"))
b=float(input("enter the secound no"))
c=float(input("enter the third no"))
if a>=b and a>=c:
    big=a
elif b>=a and b>=c:
    big=b
else:
    big=c

print("biggest no",big)