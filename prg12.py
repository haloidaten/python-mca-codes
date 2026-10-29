l1=list(map(int,input("enter the first list").split()))
l2=list(map(int,input("enter the Secound list").split()))

if len(l1) == len(l2):
    print("(a) List are of same length")
else:
    print("(a)list are not same length")

if sum(l1) == sum(l2):
    print("(b) List are of same sum")
else:
    print("(b)list are not same sum")

if any(x in l2 for x in l1 ):
    print("(c) at least one value occurs in both list")
else:
    print("(c)no common value")

