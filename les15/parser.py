import requests
import xlsxwriter
import os.path
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/newauto/marka-jeep/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
host = 'https://auto.ria.com'
cars = []


def get_html(url, params = None):
	r = requests.get(url, headers = headers, params = params)
	return r


def get_pages_count(html):
	soup = BeautifulSoup(html, 'html.parser')
	pagecount = soup.find_all('span', class_ = 'mhide')
	if pagecount:
		return int(pagecount[-1].get_text())
	else:
		return 1
	print(pagecount)

def get_content(html):
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all('div', class_ = 'proposition')
	#items2 = soup.find_all('div', class_ = 'phones_item mhide')
	for item in items:
		uah_price = item.find('span', class_ = 'grey size13')
		if uah_price:
			uah_price = uah_price.get_text(strip = True)
		else:
			uah_price = "No Price"
		cars.append({
			'title': item.find('div', class_ = 'proposition_title').get_text(strip = True),
			'link': host + item.find('h3', class_ = 'proposition_name').find_next('a').get('href'),
			'PriceInUsd': item.find('span', class_ = 'green').get_text('text', strip = True),
			'PriceInUah': uah_price,
			'City': item.find('svg', class_ = 'svg svg-i16_pin').find_next('strong').get_text('text')
		})
	for i in cars:
		html2 = get_html(i["link"])
		i['phone'] = inner_content(html2.text)
		#print("   ")
		#print(html2.text)
	print(cars)

def inner_content(html2):
	soup2 = BeautifulSoup(html2, 'html.parser')
	items2 = soup2.find_all('div', class_ = 'phones_item mhide')
	#print(items2)
	tag = soup2.find('span', class_ = 'show-phone-btn dotted')
	#print(tag.attrs.get('data-phone'))
	return tag.attrs.get('data-phone')
	#for l in cars:
	#	cars.append({
	#		'phone': tag.attrs.get('data-phone')
	#		})

def writter():
	if not os.path.exists('avtorio.xlsx'):
		workbook = xlsxwriter.Workbook('avtorio.xlsx')
		worksheet = workbook.add_worksheet()

		worksheet.write('A1', 'Марка') 
		worksheet.write('B1', 'Сылка') 
		worksheet.write('C1', 'Долоры') 
		worksheet.write('D1', 'Гривны') 
		worksheet.write('E1', 'Город') 
		worksheet.write('F1', 'Телефон') 

	workbook.close()


def parse():
	html = get_html(URL)
	if html.status_code == 200:
		#pagecount = get_pages_count(html.text)
		#print(pagecount)
		#print(cars)
		cars = get_content(html.text)
		writter()
	else:
		print('Error')

parse()