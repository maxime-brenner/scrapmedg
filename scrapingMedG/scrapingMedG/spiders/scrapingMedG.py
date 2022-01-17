from scrapy import Request, Spider, Request
from scrapingMedG.items import ScrapingmedgItem

class SpiderMedG(Spider):
	name="scrapMedG"
	starts_url="http://annuairesante.ameli.fr/trouver-un-professionnel-de-sante/medecin-generaliste/01-ain"

	def start_requests(self):
		yield Request(url=self.starts_url, callback=self.parse)

	def parse(self, response):

		 ville_list=response.css("ul.first li a::attr(href)")

		 for link in ville_list:
		 	link="http://annuairesante.ameli.fr"+link.get()
		 	print(type(ville_list))
		 	
		 	
		 	yield Request(link, callback=self.parse_attr)

	def parse_attr(self, response):
		item=ScrapingmedgItem()

		liste_med=response.css("div.item-professionnel")
		for e in liste_med:
			name=e.css("a strong::text").extract_first().strip()
			surname=e.css("a::text").extract_first().strip()
			adress_list=e.css("div.item.left.adresse::text").extract()
			adress=' '.join(adress_list)

			item=ScrapingmedgItem()
			item["name"]=name
			item["surname"]=surname
			item["adresse"]=adress

			yield item

			
			print(adress)
			

		#item["name"]=response.css("div.nom-pictos a::text").extract()



		 	

		 