import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2023/05/configurando-la-impresion-perfecta-de.html')

print(type(resultado))

#print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(sopa.select('title')[0].get_text())
print(len(sopa.select('p')))

parrafo = sopa.select('p')
print(parrafo[4].get_text())

#columna_lateral = sopa.select('.content')
#print(columna_lateral)
#columna_lateral = sopa.select('.content p')
#print(columna_lateral)

#for p in columna_lateral:
    #print(p.getText()

resultado2 = requests.get('https://www.escueladirecta.com/courses')
sopa = bs4.BeautifulSoup(resultado2.text, 'lxml')

imagenes = sopa.select('.course-box-image')[0]['src']

#for i in imagenes:
    #print(imagenes)

imagen1 = requests.get(imagenes)
#print(imagen1.content)

f = open('mi_imagen.jpg', 'wb')
f.write(imagen1.content)
f.close()

