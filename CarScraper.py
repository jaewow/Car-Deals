from lxml import html
import requests

if __name__ == "__main__":
	#Insert code for main method
	page = requests.get("https://www.autotrader.com/cars-for-sale/searchresults.xhtml?zip=75033&makeCodeList=HYUND&modelCodeList=ELANTR")
	tree = html.fromstring(page.content)
else:
	#Insert code if not being run as the main program
	print("not main method")
