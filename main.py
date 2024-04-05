from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
import time


## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")


def get_categorias(driver):
    # Esperar hasta obtener el elemento específico
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//a[contains(@href, "/supermercado")]')
        )
    )
    categorias = driver.find_elements(By.XPATH, '//a[contains(@href, "/supermercado")]')

    links_categorias = []  # Lista para almacenar los enlaces de categorías

    for categoria in categorias:
        link_categoria = categoria.get_attribute(
            "href"
        )  # Obtener el atributo href del enlace
        links_categorias.append(link_categoria)  # Agregar el enlace a la lista

    return links_categorias


def scraper():
    driver = webdriver.Firefox()
    driver.get("https://www.tiendasjumbo.co/supermercado")
    try:
        # Esperar hasta que la pagina cargue
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        get_categorias(driver)

    except Exception as e:
        print(e)


def main():
    scraper()


if __name__ == "__main__":
    main()
