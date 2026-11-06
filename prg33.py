f1 = open("C:\\Users\\USER\\Documents\\mca\\python\\s.txt", "r")
f2 = open("C:\\Users\\USER\\Documents\\mca\\python\\d.txt", "w")

lines = f1.readlines()

for i in range(len(lines)):
    if i % 2 == 0:
        f2.write(lines[i])

f1.close()
f2.close()

print("Alternate lines copied successfully!")