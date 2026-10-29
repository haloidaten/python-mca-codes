line = input("enter a line of text")
words=line.split()
wc={}
for word in words:
    wc[word]=wc.get(word,0)+1
print("word occurenceh")
for word,count in wc.items():
    print(word,":",count)