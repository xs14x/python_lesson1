#1  задание
from sys import argv
script_name,hour,perhour,plus = argv
print(script_name)
print(hour)
print(perhour)
print(plus)
hour = int(hour)
perhour = int(perhour)
plus = int(plus)
x = hour*perhour+plus
print(x)
