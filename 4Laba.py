import pytest
from selenium import webdriver
from MicrosoftMainPage import MicrosoftMainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver

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

        menu_items = {
            "Microsoft 365": "Microsoft 365 — подписка на приложения Office | Microsoft 365",
            "Teams": "Видеоконференции, собрания и звонки | Microsoft Teams",
            "Windows": "Помощь и обучение по Windows",
        }

        for item_name, expected_title in menu_items.items():
            microsoft_page.click_menu_item(item_name)
            WebDriverWait(driver, 10).until(
                EC.title_contains(expected_title.split('|')[0].strip())  # Wait until the title contains the main part
            )
            assert expected_title in driver.title
            driver.back()

        microsoft_page.click_menu_item('Поддержка')

        support_text = "Всё зорошо, я просто тестирую"
        microsoft_page.input_support_text(support_text)

        input_value = microsoft_page.get_input_value()
        assert input_value == support_text, f"Expected input value to be '{support_text}', but got '{input_value}'"
