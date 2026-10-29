num=list(map(int,input("enter the integers seperated by space").split()))
r=[x for x in num if x%2!=0]
print("list after removing even no",r)