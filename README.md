# Scraping-rappi
Este script descarga todos los nombres, precios y imagenes de los productos de Mc Donalds, que se encuentran en Rappi [https://www.rappi.com.ar/restaurantes/111443-mcdonald's-cfl-int] 
Librerias: Pandas, Pillow, Scrapy.
Para que la descarga de imagenes funcione, en el archivo settings.py agregar:

ITEM_PIPELINES={'scrapy.pipelines.images.ImagesPipeline':1} 
IMAGES_STORE = 'local_folder'
