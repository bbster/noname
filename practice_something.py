from urllib.error import HTTPError
from urllib.request import urlopen
import ssl
import re
# from bs4 import BeautifulSoup

# context = ssl._create_unverified_context()
# html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html', context=context)
# bs = BeautifulSoup(html, 'html.parser')
#
# name_list = bs.findAll('span', {'class': {'green', 'red'}})
#
# for name in name_list:
#     print(f"result_name: {name.get_text()}")
#
# title = bs.findAll(id='title', class_='text')
# print(f"result_title: {title}")

# context = ssl._create_unverified_context()
# html = urlopen('https://www.pythonscraping.com/pages/page3.html', context=context)
# bs = BeautifulSoup(html, 'html.parser')
#
# images = bs.findAll('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})
# for image in images:
#     print(f"image: {image}")
#     print(f"image_src: {image['src']}")

# for child in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
#     print(child)
# from urllib.parse import quote, unquote
# pages = set()
#
# def get_links(page_url):
#     page_url = quote(unquote(page_url))
#     global pages
#     context = ssl._create_unverified_context()
#     html = urlopen('https://ko.wikipedia.org{}'.format(page_url), context=context)
#     bs = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
#
#     for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 new_page = link.attrs['href']
#                 print(f"add_newpage: https://ko.wikipedia.org/{new_page} // {unquote(new_page)}")
#                 pages.add(new_page)
#                 get_links(new_page)
#
# get_links('')
# for link in bs.find('div', {'id': 'bodyContent'}).find_all('a', href = re.compile('^(/wiki/)((?!:).)*$')):
#
#     if 'href' in link.attrs:
#         print(f"link: {link.attrs['href']}")

# t = eval("max([1, 2, 3, 4])")
# print(t)

a = [5,4,3,2,1]

for i,x in enumerate(a):
    print(f"i:{i}")
    print(f"x:{x}")