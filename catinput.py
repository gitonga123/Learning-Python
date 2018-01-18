catNames = []

while True:
	print ('Enter the name of cat ' + str(len(catNames) + 1) + '(Or enter nothing to stop.);')
	name = raw_input()

	if name == '':
		break

	catNames = catNames + [name] #list concatenation

print ('The cat names are: ')
for name in catNames:
	print ('	' + name)

print ("Enter the pet name to determine if is in the list ")

catname = raw_input()

if catname in catNames:
	print ("You have a pet name " + catname)

else:
	print(name + ' is my pet.')
		