from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome().get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element(By.XPATH("//h5[@id='price']"), "$100")
    )
    buttonBook = browser.find_element(By.XPATH, "//button[@id='book']").click()

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.XPATH, "//input[@id='answer' and @required]").send_keys(y)

    browser.find_element(By.XPATH, "//button[@id='solve']").click()

finally:
    time.sleep(30)
    browser.quit()
