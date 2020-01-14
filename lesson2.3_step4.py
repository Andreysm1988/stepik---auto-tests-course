from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_xpath("//input[@id='answer' and @required]")
    input.send_keys(y)

    browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()


finally:
    time.sleep(30)
    browser.quit()

