import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

url = "http://books.toscrape.com/"
respuesta = requests.get(url, headers=headers)
soup = BeautifulSoup(respuesta.text, 'html.parser')

#creamos lista vacía para ir almacenando datos 
datos_libros = []

#buscamos todos los contenedores de libros 
libros = soup.find_all('article', class_='product_pod')

for libro in libros:
    #extraemos el título
    titulo = libro.h3.a['title']

    #extraemos el precio
    precio = libro.find('p',class_='price_color').text

    #limpiamos el precio (sacamos símbolo de moneda)
    precio_limpio = float(precio.replace('£', ''))

    datos_libros.append({
        "Título": titulo,
        "Precio (£)": precio_limpio
    })

#Convertimos la lista de diccionarios en un DataFrame 
df = pd.DataFrame(datos_libros)

print(df.head()) #mostramos las primeras 5 filas

#guardamos el resultado en un CSV dentro de la carpeta data/
df.to_csv('data/precios_libros.csv', index=False)
print ("\n¡Archivo guardado en data/precios_libros.csv!")