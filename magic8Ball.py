import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return 'It is certain'
	elif answerNumber == 2:
		return 'It is decidedly so'
	elif answerNumber == 3:
		return 'Yes'
	elif answerNumber ==4:
		return 'Reply Hazy try again'
	elif answerNumber == 5:
		return 'Ask again Later'
	elif answerNumber == 6:
		return 'Concentrate and ask again'
	elif answerNumber == 7:
		return 'My reply is no'
	elif answerNumber == 8:
		return 'Outlook not so good'
	elif answerNumber == 9:
		return 'Very Doubtful'
	else:
		return 'Check you input'



for i in range(10):
	r = random.randint(1,9)
	fortune = getAnswer(r)

	print (fortune)
	print("\n")