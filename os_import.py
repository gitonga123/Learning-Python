import os
totalsize = 0
for filename in os.listdir(os.getcwd()):
	totalsize = totalsize + os.path.getsize(os.path.join(os.getcwd(),filename))


print ("The total size of files stored in '" + str(os.getcwd()) + "' is " + str(totalsize)) + " KB"
