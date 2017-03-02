# Lecture 4

# # data types
# example_of_number = 123
# example_of_string = "I am string"
# example_of_list = ["Hello", "Absjfb", "wewe"]
# example_of_dictionary = {
#     "first_name": "Vasya",
#     "last_name": "Pupkin",
#     "age": 29,
#     "male": True,
#     "lucky_numbers": [6, 13, 666]
# }

# Built-in functions

# # simple math
# number_plus_number = example_of_number + example_of_number
# print(number_plus_number)
# number_plus_number += example_of_number
# print(number_plus_number)
# number_plus_number *= 2
# print(number_plus_number)
# number_plus_number = float(number_plus_number)
# print(number_plus_number)
# number_plus_number += 0.123456789
# print(number_plus_number)
# print(round(number_plus_number, 3))

# string processing
# .split() | return list of strings
# .csv
# print(example_of_string.split(","))
# .find() | return index, or -1
# print(example_of_string.find("a"))
# .replace | return string
# print(example_of_string.replace("am", "!!!!!", 3))
# print(example_of_string.s())

# list processing
# example_of_list.append([1, 2, {"hasdf": "sdfsdf"}])
# example_of_list.append("new one 2")
# print(example_of_list)
# print(example_of_list)
# example_of_list.insert(2, "one more")
# print(example_of_list)
# example_of_list.insert(2, "one more 2")
# print(example_of_list)
# print(example_of_list.index("one mojgkgjhre"))
# print(example_of_list)
# # # print(example_of_list.index("qwe"))
# print(example_of_list.pop(34785346))
# print(example_of_list)
# example_of_list.sort(key=)
# print(example_of_list)

# dict processing
# print(example_of_dictionary.items())  # list of tuples
# print(example_of_dictionary.values())  # list of values
# print(example_of_dictionary)
# example_of_dictionary["new_key"] = "some new value"
# print(example_of_dictionary)
# new_data_in_dict = {"single": False, "handsome": True, "phone": "+123 456 7890"}
# example_of_dictionary.update(new_data_in_dict)
# print(example_of_dictionary)
# example_of_dictionary.pop("new_key")
# print(example_of_dictionary)
#

# "I, am, learning, Python"
# ["I", "am", "learning", "Python"]
# {
#   "key": "I",
#   "key2": "am",
#   "key3: "learning"
# }
# key, key2, key3 -> ["I", "am", "learning"]
# ["I", "am"].sort()
# ["am", "I"] -> sorted list of previous

# statements | indentation(!)
# <, >, !=, ==, is, not, or, and

# learn = "asdasdas"
#
# if type(learn) is set:
#     print("Str")
# else:
#     print("other")

# from test_module import example
# import test_module
# from test_module import *
# from test.test_module import example, awesome_string
# from random import randint, choice
# import string
# import uuid
# import datetime
# import time
# import os
# import subprocess
#
# rand_words[2]
# print(string.ascii_letters)
# rand_word = choice(rand_words)
# example(rand_word)


# rand_words = ["hello", "hi", "greetings", "hallo"]
rand_words = "he!#%^$#@ llo"
num = 123

for index in range(10):
    num += 1

    print(num)















