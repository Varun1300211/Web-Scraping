#import requests
#url = "https://google.com"
#r = requests.get(url)		# r variable has all the HTML code
#htmlContent = r.content	# r returns response so if we want the code we write r.content
#print(htmlContent)		# printing the code
#htmlText = r.text
#print(htmlText)

import requests
from bs4 import BeautifulSoup
url = "https://google.com"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

print(soup.prettify())	# to print html in tree structure
