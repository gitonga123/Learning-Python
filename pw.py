# password manager python

#! python2

PASSWORDS = {'email': 'mutwiridanielsci@gmail.com','blog':'qwdjajbsakaijcasjbba','luggage':'1234512345'}

import sys

if len(sys.argv) < 2:
	print('Usage: Python pw.py[account] - copy account password')
	sys.exit()

account = sys.argv[1]