from bs4 import BeautifulSoup
import dryscrape
import time

def links_scraper(pages):
	my_url = "http://www.emol.com/nacional/"
	session = dryscrape.Session()
	session.set_attribute('auto_load_images', False)
	session.set_error_tolerant(True)
	session.visit(my_url)
	links = []
	for i in range(0,pages):
		#session.render("emol"+str(i)+".png")
		response = session.body()
		tmp = []
		soup = BeautifulSoup(response,"lxml")
		news = soup.find_all("div",{"id":"listNews"})[0]
		for a in news.find_all('a',href=True):
			tmp.append(a['href'])
		news_norep = []
		for j in range(0,len(tmp)):
			if j%3==0:
				news_norep.append(tmp[j])
		#print(news_norep)
		links.append(news_norep)
		next_button = session.at_xpath('//*[contains(text(), "Siguiente")]')
		next_button.double_click()
		time.sleep(1)
		
	return links