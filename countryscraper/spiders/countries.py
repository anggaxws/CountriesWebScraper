#importing the scrapy library
import scrapy

#Creating the Spider Class
class CountriesSpider(scrapy.Spider):
    name = "countries"
    start_urls = ['https://www.scrapethissite.com/pages/simple/']
    
    #Parsing the Response, this is swhere the spider processes the webpage content and extracts the desired data.
    def parse(self, response):
        #Extracting Data
        for country in response.css('div.col-md-4.country'):
            population = country.css('span.country-population::text').get().replace(',', '')
            area = country.css('span.country-area::text').get().replace(',', '')

            # Clean and convert data
            population = int(population) if population.isdigit() else None
            try:
                area = float(area)
            except ValueError:
                area = None
                
            #This sends the extracted data as a Python dictionary
            yield {
                'name': country.css('h3.country-name::text').get().strip(),
                'capital': country.css('span.country-capital::text').get(),
                'population': population,
                'area': area,
            }
