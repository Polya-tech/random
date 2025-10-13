from components.components import WebElement
from pages.base_page import BasePage

class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, '#currentAddress')
        self.btn_submit = WebElement(driver, '#submit')
        self.output_full_name = WebElement(driver, '#name')
        self.output_current_address = WebElement(driver, '#output #currentAddress')





from pages.text_box_clear import TextBox
import time

def test_clear(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.full_name.send_keys('testirovich')
    text_box.current_address.send_keys('Moscow')
    text_box.btn_submit.click()
    time.sleep(1)


   
    # assert text_box.current_address.get_dom_attribute('value') == 'Moscow'
    # assert text_box.output_full_name.exist()
