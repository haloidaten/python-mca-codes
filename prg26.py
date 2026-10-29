sq=lambda s:s*s
rec=lambda l,b:l*b
tri=lambda base,hi:0.5*base*hi

s=float(input("entr the side of sq:"))
print("area of squre",sq(s))


l=float(input("entr the length of rect:"))
b=float(input("entr the breth of rect:"))
print("area of rect",rec(l,b))

hi=float(input("entr the height of tri:"))
base=float(input("entr the base of tri:"))
print("area of tri",tri(hi,base))
