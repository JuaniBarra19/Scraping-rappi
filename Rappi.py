import scrapy
from datetime import datetime 
import pandas as pd

 


now = datetime.now() 
current_time = now.strftime("%d-%m-%Y") # Formato de fecha para crear una columna desp


# Name
XPATH_MCcombos = "//*[@id]/div//h4/text()"


# Price
XPATH_Precio = "//*[@id]//div[@class='styles__PriceoContainer-sc-jkotxm-5 dxkArC']/span[1]/text()" 






class Spider(scrapy.Spider):

    name = 'Rappi23'
    start_urls = [
        "https://www.rappi.com.ar/restaurantes/111443-mcdonald's-cfl-int"
    ]

    custom_settings={
        'FEED_URI': 'URLimagenes.csv', 
        'FEED_FORMAT': 'csv', 
        'FEED_EXPORT_ENCODING': 'utf-8'
    } 


    
    def parse(self, response):
        
        nombres = response.xpath(XPATH_MCcombos).getall()
        precios = response.xpath(XPATH_Precio).getall()    
        raw_image_urls = response.xpath("//*[@id]//img[@data-testid='image']/@src").getall()
        clean_image_urls=[]  
        
        for img_url in raw_image_urls:
            clean_image_urls.append(response.urljoin(img_url))
        
        yield {
            'image_urls': clean_image_urls
        }

        df = pd.DataFrame(list(zip(nombres,precios)),columns = ['Nombre','Precio']) 
        print(df) 

        df.to_csv('Rappi.csv', index=False) 

    