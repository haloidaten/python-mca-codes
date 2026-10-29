n = input("enter first name separated by space").split()
c = sum(name.lower().count('a') for name in n)
print("number of occurrences of 'a'", c)
