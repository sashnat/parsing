# изменено для Python3 на основании http://python-3.ru/page/parser-html-python, с корректировками и дополнениями

# pip3 install bs4
# pip3 install lxml
# pip3 install html5lib

from bs4 import BeautifulSoup
from urllib.request import urlopen

f1 = open("file1.txt", "w")
f2 = open("file2.txt", "w")
f3 = open("file3.txt", "w")
f4 = open("file4.txt", "w")

# В результате выполнения скрипта должны получить структурированный код сайта
html_doc = urlopen('http://python-3.ru').read()
soup = BeautifulSoup(html_doc)
print (soup)
for line in soup:
    print(soup)
    f1.write(str(line))

print (soup.title) # <title>Python 3 - Программирование на Python 3</title>
print (soup.title.string) # Python 3 - Программирование на Python 3

print("----------------------------Cодержимое мета полей-----------------------------------")
for meta in soup.find_all('meta'):
    m = meta.get('content')
    print(m, type(m))
    #f2.write(str(m))    # запись в файл без разделения на строки
    print(m, file = f2)  # записывется в файл построчно

print("----------------------------Поиск по ссылкам-----------------------------------")
for link in soup.find_all('a'):
    l = link.get('href')
    print(l)
    #f3.write(str(l))    # запись в файл без разделения строк
    print(l, file = f3)  # записывется в файл построчно
print("----------------------------Содержимое ссылок-----------------------------------")
for link in soup.find_all('a'):
    c = link.contents[0]
    print(c)
    f4.write(str(c))
    print(c, file = f4)  # записывется в файл построчно
print("----------------------------Парсер DIV блоков-----------------------------------")
# Содержимое из <div class="content"> ... </div>
print (soup.find('div', 'content'))

# Блок: <div id="top_menu"> ... </div>
print (soup.find('div', id='top_menu'))

print("----------------------------Ссылки на изображения-----------------------------------")
for img in soup.find_all('img'):
    print (img.get('src'))

f1.close()
f2.close()
f3.close()
f4.close()
