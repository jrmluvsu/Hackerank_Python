from math import asin, pi,degrees, atan2
ab = int(input())
bc = int(input())
ac = (ab**2 + bc**2)**0.5
mc = ac/2
theta = asin((mc/bc))
#print(f"{round((theta*180)/pi)}"+u"\N{DEGREE SIGN}")
print(f"{round(degrees(atan2(ab,bc)))}"+u"\N{DEGREE SIGN}")