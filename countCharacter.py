import pprint
print('Enter the string you want to count the number of characters in. ')

message = raw_input()
count = {}

for n in message:
	count.setdefault(n,0)
	count[n] =count[n] + 1

print(pprint.pformat(count))
