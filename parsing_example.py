# на основании http://python-3.ru/page/parser-html-python с корректировками для Python3

# pip3 install bs4
# pip3 install lxml
# pip3 install html5lib


from bs4 import BeautifulSoup
from urllib.request import urlopen

# В результате выполнения скрипта должны получить структурированный код сайта
html_doc = urlopen('http://python-3.ru').read()
soup = BeautifulSoup(html_doc)
print (soup)

print (soup.title) # <title>Python 3 - Программирование на Python 3</title>
print (soup.title.string) # Python 3 - Программирование на Python 3

print("----------------------------Cодержимое мета полей-----------------------------------")
for meta in soup.find_all('meta'):
    print(meta.get('content'))

print("----------------------------Поиск по ссылкам-----------------------------------")
for link in soup.find_all('a'):
    print (link.get('href'))

print("----------------------------Содержимое ссылок-----------------------------------")
for link in soup.find_all('a'):
    print (link.contents[0])

print("----------------------------Парсер DIV блоков-----------------------------------")
# Содержимое из <div class="content"> ... </div>
print (soup.find('div', 'content'))

# Блок: <div id="top_menu"> ... </div>
print (soup.find('div', id='top_menu'))


print("----------------------------Ссылки на изображения-----------------------------------")
for img in soup.find_all('img'):
    print (img.get('src'))
