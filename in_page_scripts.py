from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


def send_page_up(driver: WebDriver):
    """Sube la pagina"""
    driver.execute_script("window.scrollBy(0, -window.innerHeight);")


def scroll_down(driver: WebDriver, wait_time: int = 10):
    """A method for scrolling the page."""

    # Scroll to the middle of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
    time.sleep(wait_time)  # Esperar un momento

    # Scroll to the bottom of the page in two stages
    for _ in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(wait_time)  # Esperar un momento

    # Implement your loop for gradual scrolling
    y = 1000
    for _ in range(7):
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 1000
        time.sleep(2)  # Esperar 1 segundo


def go_to_page(driver: WebDriver, page_number: int) -> None:
    """Va al numero de pagina que se le pase como parametro, es decir el argumento page_number"""

    send_page_up(driver)
    time.sleep(2)
    next_page = driver.find_element(
        By.XPATH,
        f'//button[contains(@class, "tiendasjumboqaio-jumbo-fetch-more-paginator-0-x-buttonPerPage") and text()="{page_number}"]',
    )

    if next_page:
        ActionChains(driver).click(next_page).perform()
