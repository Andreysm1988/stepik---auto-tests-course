from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_xpath("//input[@id='answer' and @required]")
    input1.send_keys(y)

    checkbox = browser.find_element_by_xpath("//input[@id='robotCheckbox' and @required]")
    checkbox.click()

    radio = browser.find_element_by_xpath("//input[@id='robotsRule']")
    radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
