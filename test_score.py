from __future__ import print_function

first_score = int(input("Enter the first mark "))
second_score = int(input("Enter the Second Mark "))
third_score = int(input("Enter the Last score "))
highest_score = 95

total = (first_score + second_score + third_score)/3

print("Your average Marks is ", total)

if total >= 95:
	print("Congratulations!")
	print("Your Average is great")


exam_card = 1000.578

print("Your fee Balance is ", format(exam_card, ',.2f'))
	