# class Human:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def say_something(self):
#         return "JKHGDJKDG"
#         # raise NotImplementedError("Can't find that method")
#
#
# class Man(Human):
#     def say_something(self):
#         return "Hello, i'm man."
#
#
# class Woman(Human):
#     def say_something(self):
#         return "Hey, i'm woman."
#     _qwerty = ""
#
#
# class Kid(Human):
#     pass
#
# man = Man("John", "Doe")
# woman = Woman("Marry", "Smith")
# kid = Kid("Jack", "Nicholson")
# print(man.say_something())
# print(woman.say_something())
# print(kid.say_something())
#


# class Man(object):
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def say_something(self):
#         print(self.__work())
#         return "Hello, i'm man."
#
#     def __work(self):
#         return "Working..."
#
#
#
# man = Man("John", "Doe")
#
# print(man.say_something())
# man.__work()


# class Man(object):
#     __age = 0
#
#     def __init__(self, first_name, last_name):
#         self._age = 28
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def get_age(self):
#         return "{} year(s) old.".format(self._age)
#
# man = Man("John", "Doe")
#
# print(man.first_name, man.last_name)
# print(man.get_age())
# print(man._age)
# man._age = 32
# print(man._age)
# print(man.get_age())


# metaclass(Animal)
# class(CatFamily)
# obj(Cat)


# class RevealAccess(object):
#     def __init__(self, init_val, name):
#         self.val = init_val
#         self.name = name
#
#     def __get__(self, obj, obj_type):
#         print('Get value', self.name)
#         return self.val
#
#     def __set__(self, obj, val):
#         print('Set value', self.name)
#         self.val = val
#
#
# class MyClass(object):
#     x = RevealAccess(10, 'var "x"')
#     y = 5
#
# m = MyClass()
# print(m.x)
# m.x = 11
# print(m.x)
# print(m.y)


# m.x -> __get__ [x, 10] -> return
# m.x -> __set__ [x, VALUE] -> return


# class ExampleIterator(object):
#     def __init__(self, filename):
#         self.fd = open(filename, 'r')
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         line = self.fd.readline()
#         if line != '':
#             line = line.rstrip('\n')
#             self.line = line.upper()
#             return self.line
#         raise StopIteration
#
#     def test(self):
#         # line = self.fd.readline()
#         return "HELLO from {}".format(self.line.lower()*2)
#
#
# file_data = ExampleIterator("test.txt")
# print(file_data.__next__())
# print(file_data.__next__())
# print(file_data.test())
# print(file_data.__next__())
# print(file_data.__next__())

# print(file_data)
# for item in file_data:
#     print(item)
#
# print("------------")
#
# for line in open("test.txt").read().splitlines():
#     print(line)


# class ExampleIterator(object):
#
#     def __init__(self, items):
#         self.items = items
#         self.count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         try:
#             self.item = self.items[self.count]
#             self.count += 1
#             return self.item
#         except IndexError:
#             raise StopIteration
#
#     def test(self):
#         return "HELLO from {}".format(self.item)
#
#
# file_data = ExampleIterator(["asd", "qwe", "zxc"])
# print(file_data.__next__())
# print(file_data.__next__())
# print(file_data.test())

# def power(start):
#     for i in range(start, start+5):
#         yield i*i
#
# print(power(5))
#
# for item in power(5):
#     print(item)
#
# for item in [25, 36...]:
#     print(item)
# test = []
# for x in range(20):
#     x = x * 2  # [#asd #dfklg = #asd * 2]
#     test.append(x)


# test = [x for x in range(20) if x > 5]
# print(test, type(test))

# import csv
# with open('eggs.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    # spamwriter.writehe
    # spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

import csv
with open('eggs.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["First", "Last", "Age"])
    writer.writeheader()
    writer.writerow({"First": "John",
                     "Last": "Smith",
                     "Age": "29"})
