age = input("Age of the Dog: ")

print

if age < 0:
	print "This can hardly be true!"
elif age == 1:
	print "About 14 human years"
elif age == 2:
	print "About 22 human years"
elif age > 2 :
	human = 22 + (age - 2) * 5
	print "Human Years: ", human

raw_input('press Return>')