from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MicrosoftMainPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_page(self):
        self.driver.get("https://www.microsoft.com/ru-ru")

    def click_menu_item(self, item_name):
        menu_item = self.driver.find_element(By.LINK_TEXT, item_name)
        menu_item.click()

    def input_support_text(self, support_text):
        support_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "supHomeAndLandingPageSearchBox"))
        )
        support_input.clear()
        support_input.send_keys(support_text)

    def get_input_value(self):
        support_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "supHomeAndLandingPageSearchBox"))
        )
        return support_input.get_attribute("value")