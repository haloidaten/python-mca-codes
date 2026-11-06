class time:
    def __init__(self,h,m,s):
        self._h=h
        self._m=m
        self._s=s
    def __add__(self,other):
        t_s=self._s+other._s
        t_m=self._m+other._m
        t_h=self._h+other._h

        t_m += t_s//60
        t_s = t_s %60
        t_h += t_m//60
        t_m = t_m %60

        return time(t_h,t_m,t_s)
    def display(self):
        print(self._h,"hours")
        print(self._m,"minuites")
        print(self._s,"secounds")

t1=time(2,45,50)
t2=time(1,30,25)
t3=t1+t2
print("first time")
t1.display()
print("secoundtime")
t2.display()
print("thirdtime")
t3.display()
