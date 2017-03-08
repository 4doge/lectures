# - while (continue / break / else)

# counter = 0
#
# while counter < 10:
#     counter += 1
#     if counter == 5:
#         continue
#     print("Counter - ", counter)
# else:
#     print("Finished")


# - try/except/else/finally

# example = [1, 2, 3]
#
# try:
#     print(example[1])
# except ValueError:
#     print("Value error")
# except IndexError:
#     print("Index error")
# else:
#     print(example[2])
# finally:
#     print("Finally")


# pip
# pip freeze
# pip install <package_name>
# pip install <package_name>==1.0.1b4
# pip uninstall <package_name>


# pip install virtualenv
# virtualenv ENV
# virtualenv venv
# source ENV/bin/activate
# deactivate
# pip freeze > requirements.txt
# pip install -r requirements.txt
# pip freeze | xargs pip uninstall -y

# import requests
#
# API_ENDPOINT = "http://ip-api.com/json/54.34.12.10"
#
# r = requests.get(API_ENDPOINT)
# data = r.json()
# print(data.get("qewqweqweqwe"))
# if data.get("qewqweqweqwe"):
#     print("REAL")
# else:
#     print("NONE")
#
# print(data.get("country"))

# requirements/dev.txt
# local.txt
# prod.txt
