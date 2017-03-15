from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import os
from datetime import datetime

# http://selenium-python.readthedocs.io/installation.html#drivers
chromedriver = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver")
# phantomjsdriver = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phantomjs")
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
# driver = webdriver.PhantomJS(phantomjsdriver)

driver.get("http://toster.ru")

# driver.set_window_size(100, 100)
# driver.set_window_position(100, 100)
# driver.maximize_window()

topics = driver.find_elements_by_class_name("question_short")

for topic in topics:
    title_element = topic.find_element_by_class_name("question__title-link")
    title = title_element.text

    url = title_element.get_attribute("href")

    subscribers = topic.find_element_by_class_name("question__views-count").text.split()[0]

    published_string = topic.find_element_by_class_name("question__date_publish").get_attribute("datetime")
    published_datetime = datetime.strptime(published_string, "%Y-%m-%d %H:%M:%S")
    published = published_datetime.strftime("%d-%m-%Y")

    answers = topic.find_element_by_class_name("mini-counter__count_grey").text

    try:
        topic.find_element_by_class_name("icon_check")
        has_correct_answer = True
    except NoSuchElementException:
        has_correct_answer = False

    data = {
        "title": title,
        "url": url,
        "subscribers": subscribers,
        "published": published,
        "answers": answers,
        "has_correct_answer": has_correct_answer
    }
    print(data)


search_input = driver.find_element_by_name("q")
search_input.send_keys("python" + Keys.RETURN)

driver.execute_script("window.scrollTo(0, 500);")

driver.find_element_by_class_name("btn_add-question").click()
driver.find_element_by_class_name("empty-block__button").click()

driver.find_element_by_xpath("//input[@name='email']").send_keys("test@gmail.com")
driver.find_element_by_xpath("//input[@name='password']").send_keys("s3cr3t")
driver.find_element_by_xpath("//button[@type='submit']").click()


# driver.quit()
