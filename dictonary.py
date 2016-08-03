#A dictonary is an object that stores a collection of data. Each element
#in a dictonary has tow parts: A Key and a Value. You use a key to locate
# a specific value
#Key-Value pairs are often referred to as mappings because each key
#is mapped to a value.
#A KeyError exception is raised if you try to retrieve a value from
#a dictionary using a nonexistent key.
phonebook = {'Daniel':'0710594287', 'James':'657382123','mathews':'0997563','Lawrence':'09834261'}
if 'Daniel' in phonebook:
	print(phonebook['Daniel'])
	phonebook['Joe'] = '555-0123'
	phonebook['Chris'] = '555-444'
	
	for key in phonebook:
		print key, phonebook[key]
		pass
	#Getting the Number of Elements in a Dictonary
	num_items = len(phonebook)
	print num_items


	#further Manipulation
	test_scores = {'Kyla':[88,92,100],'sophie':[95,74,81],'Ethan':[70,88,91,45],'Luis':[70,56,34]}
	print test_scores
	test_sophie = test_scores['Kyla']
	print len(test_sophie)
	total =0 
	for value in test_sophie:
		total +=value
		pass
	print total
	pass

#get can be used instead[] to get the value of a key
value = phonebook.get('Joe', 'Entry not found')
print value

for key, value in phonebook.items():
	print key, value

for key in phonebook.keys():
	print key

