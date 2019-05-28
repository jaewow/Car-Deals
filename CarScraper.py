from lxml import html
import requests

if __name__ == "__main__":
	#Insert code for main method
	page = requests.get("https://www.autotrader.com/cars-for-sale/searchresults.xhtml?zip=75033&makeCodeList=HYUND&modelCodeList=ELANTR")
	tree = html.fromstring(page.content)
	script = tree.xpath('//*[@id="mountNode"]/div/div[3]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/script[4]/text()')
	print(script)
else:
	#Insert code if not being run as the main program
	print("not main method")
