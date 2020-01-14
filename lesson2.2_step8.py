from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//input[@name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//input[@name='email']")
    input3.send_keys("Smolensk@mail.ru")

    file_button = browser.find_element_by_xpath("//input[@name='file']")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_path = os.path.join(current_dir, '228.txt')
    file_button.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()