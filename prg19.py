
s = int(input("Enter starting num: "))
e = int(input("Enter ending num: "))

for n in range(s, e + 1):
    if 1000 <= n <= 9999:
        digits = str(n)

        if all(int(d) % 2 == 0 for d in digits):
            root = int(n ** 0.5)

            if root * root == n:
                print(n)
