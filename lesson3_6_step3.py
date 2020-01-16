import time
import math
import pytest
from selenium import webdriver


def get_answer():
    answer = str(math.log(int(time.time())))
    return answer


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, url):
    a = get_answer()
    link = f"https://stepik.org/lesson/{url}/step/1"
    browser.get(link)
    time.sleep(3)
    browser.find_element_by_xpath("//textarea").send_keys(a)
    browser.find_element_by_xpath("//button[@class='submit-submission']").click()
    time.sleep(5)
    correct = browser.find_element_by_xpath("//pre[@class='smart-hints__hint']")
    print(correct.text)
    assert correct.text == "Correct!"
