num=list(map(int,input("Enter integers seperated by space:").split()))
r=['over' if x>100 else x for x in num]
print("result",r)
         