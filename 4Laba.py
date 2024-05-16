import pytest
from selenium import webdriver
from MicrosoftMainPage import MicrosoftMainPage

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()  
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
class TestMicrosoftSite:
    def test_navigation_and_input(self, driver):
        microsoft_page = MicrosoftMainPage(driver)
        microsoft_page.navigate_to_page()

        initial_url = driver.current_url

        menu_items = ["Microsoft 365", "Teams", "Windows"]
        for item_name in menu_items:
            microsoft_page.click_menu_item(item_name)
            driver.back()

        microsoft_page.click_menu_item('Поддержка')

        support_text = "Всё зорошо, я просто тестирую"
        microsoft_page.input_support_text(support_text)
