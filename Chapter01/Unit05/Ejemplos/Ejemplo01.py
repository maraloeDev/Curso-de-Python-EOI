year = int(input("Introduce un año: "))
leap_year = (year % 4 ==0 and year % 100 !=0) or year % 400 == 0
print(leap_year)