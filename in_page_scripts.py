from selenium.webdriver.firefox.webdriver import WebDriver
import time


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
