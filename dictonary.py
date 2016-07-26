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
	print(phonebook)
	pass
