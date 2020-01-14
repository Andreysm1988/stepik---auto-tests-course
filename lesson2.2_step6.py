from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(a):
    return str(math.log(abs(12*math.sin(int(a)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print('x= ', x)
    result = calc(x)
    print('result= ', result)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("window.scrollBy(0, 100);")

    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
