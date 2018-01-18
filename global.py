global eggs
def spam():
	global eggs
	eggs = 'spam'
	print eggs


eggs = "Kuku Eggs"
spam()
print(eggs)