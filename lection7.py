from datetime import datetime, timedelta


# now = datetime.now()
#
# print(now.year)
# print(now.month)
# print(now.day)
#
# # birthday = "{}/{}/{}".format(now.month, now.day, now.year)
# # print(birthday)
#
# formatted_now = now.strftime("[%H:%M] %m/%d/%Y %p")
#
# print(formatted_now, type(formatted_now))


# birthday = input("Enter your birthday (YYYY-MM-DD): ")
# print(birthday, type(birthday))
# date_format = "%Y-%m-%d"
# datetime_birthday = datetime.strptime(birthday, date_format)
# print(datetime_birthday, type(datetime_birthday))
# print(datetime_birthday.year)
# if datetime_birthday.year < 1999:
#     print("ALLOW")
# else:
#     print("REJECT")


# now = datetime.now()
# friend_birthday = now + timedelta(days=12)
#
# # datetime.date
# # 00:00:00
#
# if now.date() == friend_birthday.date() - timedelta(days=12):
#     print("Today")
# else:
#     print("NOT TODAY")


# Friends birthday reminder
# some_date = "12:03:2017"
# some_date_formatted = datetime.strptime(some_date, "%d:%m:%Y")
#
# now_date = datetime.now().date()
# if now_date + timedelta(days=-7) < some_date_formatted.date() < now_date + timedelta(days=7):
#     print("In range")
# else:
#     print("Not in range")
#
#
#
# import logging
#
# logging.basicConfig(filename='example.log', filemode='w',
#                     format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
#                     level=logging.CRITICAL)
#
# logging.info("Info message")
#
# logging.debug("Debug message")
# logging.error("Error message")
# logging.critical("Critical message")
#
# """
# INFO: info, warning, error, critical
# WARNING: warning, error, critical
# DEBUG: info, warning, debug, error, critical
# ERROR: error, critical
# CRITICAL: critical
# """
#

# python test.py -i test.txt test2.txt

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-f", dest="first_name",
                    help="input first", metavar="first")
parser.add_argument("-l", dest="last_name",
                    help="input last")

args = parser.parse_args()

print(args)
print(args.first_name)
print(args.last_name)





