import unittest
from selenium import webdriver


link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
answer_accept = "Congratulations! You have successfully registered!"
browser = webdriver.Chrome()


class TestPages(unittest.TestCase):
    def test_page1(self):
        browser.get(link1)
        input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
        input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
        input3 = browser.find_element_by_xpath("//input[@class='form-control third' and @required]")
        button = browser.find_element_by_css_selector("button.btn")
        input1.send_keys("Ivan")
        input2.send_keys("Petrov")
        input3.send_keys("Petrov@mail.ru")
        button.click()
        answer = browser.find_element_by_tag_name("h1")
        answer_text = answer.text
        print('1')
        self.assertEqual(answer_text, answer_accept, "Fail")

    def test_page2(self):
        browser.get(link2)
        input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
        input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
        input3 = browser.find_element_by_xpath("//input[@class='form-control third' and @required]")
        button = browser.find_element_by_css_selector("button.btn")
        input1.send_keys("Ivan")
        input2.send_keys("Petrov")
        input3.send_keys("Petrov@mail.ru")
        button.click()
        answer = browser.find_element_by_tag_name("h1")
        answer_text = answer.text
        print('2')
        self.assertEqual(answer_text, answer_accept, "Fail")


if __name__ == "__main__":
    unittest.main()