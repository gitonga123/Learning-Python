from __future__ import print_function

print("Car Speed Converted from KPH to MPH")
print("KPH\tMPH")
print("___________")

for speed in range(0,181,10):
	speed_mph = speed * 0.6214
	print(speed, "\t",format(speed_mph, '.0f'))
	pass