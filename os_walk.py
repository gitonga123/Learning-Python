import os
from termcolor import colored

for folderName, subfolders, filenames in os.walk(os.path.join('/home','daniel','Desktop','Learning_python')):
	print colored(('The Current Folder is: ' + folderName),'red')

	for subfolder in subfolders:
		print colored(('SUBFOLDER OF: ' + folderName + ':' + subfolder),'yellow')

	for filename in filenames:
		print colored(('FILE INSIDE ' + folderName + ': '+ filename),'white')
