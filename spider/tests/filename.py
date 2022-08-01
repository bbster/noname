import ssl
from urllib.parse import quote
from urllib.request import urlopen

page_url = '/wiki/위키백과:파일_올리기'
page_url = quote(page_url)
context = ssl._create_unverified_context()
html = urlopen('https://ko.wikipedia.org{}'.format(page_url), context=context)
