high_score = 95

test1 = int(input('Enter the score for  test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 2: '))

average = (test1 + test2 + test3)/3

print('The Average score is', format(average, '.2f'))

if average >= high_score:
	print("CONGRATULATIONS!")
	print("That is a great average")


