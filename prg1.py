import datetime
c_year = datetime.datetime.now().year
f_year = int(input("Enter the year"))
print("leap years from",c_year,"to",f_year,".")
for year in range(c_year,f_year+1):
    if (year % 400 == 0 )or (year % 4==0 and year %100 !=0):
         print(year)