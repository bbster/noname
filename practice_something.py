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

# a = [5,4,3,2,1]
#
# for i,x in enumerate(a):
#     print(f"i:{i}")
#     print(f"x:{x}")
#
# def number_generator():
#     yield 0
#     yield 1
#     yield 3
#
# for i in number_generator():
#     print(i)

# g = number_generator()
# print(dir(g))
# print(dir(range))
#
# class FourCalc:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#
#     def add(self):
#         result = self.first + self.second
#         return result
#
#     def minus(self):
#         result = self.first - self.second
#         return result
#
# a = FourCalc(4,2)
#
# print(a.minus())

# call by value / call by reference

call_by_value = 10
call_by_reference = [1,2,3,4]


def test_value_id(some_value):
    print(f"some_value_before: {id(some_value)}")
    some_value = 5
    print(f"some_value_after: {id(some_value)}")


def test_reference_id(some_reference):
    print(f"some_reference_before: {id(some_reference)}")
    some_reference = [5,6,7,8]
    print(f"some_reference_after: {id(some_reference)}")

# test_value_id(call_by_value)
# print(f"call_by_value: {id(call_by_value)}")
# test_reference_id(call_by_reference)
# print(f"call_by_reference: {id(call_by_reference)}")

#
# def parameter_func(*args, **kwargs):
#     # for i in args:
#     #     print(i)
#     # for j in kwargs:
#     #     print(kwargs)
#     # print(args)
#     # print(kwargs.get("nothing", default=0))
#     # print(kwargs.items())
#     print(kwargs.setdefault("nothing", ))
#     print(dir(kwargs))
#
#
# parameter_func(4,2,5, name="tester", age=6)
#
# li = set()
# print(type(li))


class A():
    some_attribute = "something"
    def __init__(self, title):
        self.title = title

    def show(self):
        print(self.title)

class B(A):

    def __init__(self, title, something):
        super().__init__(title)
        super().some_attribute
        self.something = something
        print(something)

a = A("title")
b = B("title", "Something")
b.show()

class Car():
    ud = "운전대 입니다." # 초기 default

    # def __init__(self, door, wheel):
    #     self.door = door   # api 외부 데이터에 의해 변경될 attribute
    #     self.wheel = wheel

    @staticmethod
    def get_instance():
        a = Car(4,4)
        return a

class Validation():

    @staticmethod
    def validate(Car):
        if Car.ud == "운전대 입니다.":
            return Car.ud
        else:
            print("운전대 아닙니다.")

print(Validation.validate(Car()))
# a = Car(4,4)
# a.get_instance()
# Car.get_instance()
# print(Car.get_instance())
# print(a.get_instance())
