w=input("enter a string")
if w.endswith("ing"):
    w = w + "ly"
else:
    w=w+"ing"
    
print(w)
