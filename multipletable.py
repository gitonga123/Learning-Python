''' Python program to find the
multiplication table (from 1 to 10)'''

num = int(input("Enter any number to create its multiplication table: "))
uprange = int(input("Enter the highest multiple in the table: ")) 
# To take input from the user
# num = int(input("Display multiplication table of? "))

# use for loop to iterate 10 times
for i in range(1, uprange+1):
   print(num,'x',i,'=',num*i)