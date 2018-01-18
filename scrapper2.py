# Importing the dependencies
# This is needed to create a lxml object that uses the css selector
from lxml.etree import fromstring

import requests, json

API_URL = 'https://www.sportpesa.com/?sportId=1&todaygames=1'
scraped_stores = []


