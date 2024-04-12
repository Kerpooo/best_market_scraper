from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.webdriver import WebDriver
import traceback
from in_page_scripts import scroll_down


## Setup firefox options
options = webdriver.FirefoxOptions()
options.add_argument("-headless")  # GUI off


def get_productos(driver: WebDriver) -> list[WebElement]:
    """Obtiene la lista de todos los productos de la pagina actual"""

    scroll_down(driver, 10)

    productos_list = driver.find_elements(
        By.XPATH, '//a[contains(@class, "vtex-product-summary-2-x-clearLink")]'
    )

    return productos_list


def productos_to_dict(nombre, precio, marca) -> dict[str, str]:
    producto = {"nombre_producto": nombre, "precio": precio, "marca": marca}
    return producto


def get_productos_data(productos_list: list[WebElement]) -> list[dict[str, str]]:
    """Obtiene las caracteristicas de cada uno de los productos
    y los pasa a un diccionario"""

    productos_data_list = []
    for producto in productos_list:
        nombre_producto = producto.find_element(
            By.XPATH,
            './/h2/span[contains(@class, "vtex-product-summary-2-x-productBrand")]',
        ).text

        precio_producto = producto.find_element(
            By.XPATH,
            './/div[contains(@class, "tiendasjumboqaio-jumbo-minicart-2-x-price")]',
        ).text

        marca_producto = producto.find_element(
            By.XPATH,
            './/span[contains(@class, "vtex-product-summary-2-x-productBrandName")]',
        ).text

        producto = productos_to_dict(nombre_producto, precio_producto, marca_producto)

        productos_data_list.append(producto)

    return productos_data_list


def get_cantidad_paginas(driver: WebDriver) -> int:
    """Obtiene la cantidad de paginas que se tiene, especificamente la parte de paginación.
    Devuelve un entero"""

    scroll_down(driver)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '//select[contains(@style, "appearance: menulist-button")]')
        )
    )

    paginas_container = driver.find_element(
        By.XPATH, '//select[contains(@style, "appearance: menulist-button")]'
    )

    paginas_list = paginas_container.find_elements(
        By.XPATH, ".//option"
    )  # Cambiado el XPath aquí
    return len(paginas_list)


def get_categorias(driver: WebDriver) -> list[str]:
    """Obtiene las categorias de la pagina principal.
    Devuelve una lista con las url's de cada una de las categorias.
    """
    scroll_down(driver)

    # Esperar hasta obtener el elemento específico
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//a[contains(@href, "/supermercado")]')
        )
    )
    categorias = driver.find_elements(By.XPATH, '//a[contains(@href, "/supermercado")]')

    # Lista para almacenar los enlaces de categorías
    links_categorias = []

    for categoria in categorias:
        link_categoria: str = categoria.get_attribute("href")
        # Obtener el atributo href del enlace
        links_categorias.append(link_categoria)  # Agregar el enlace a la lista

    return links_categorias


def scraper(url: str) -> WebDriver:
    driver = webdriver.Firefox(options)
    driver.get(url)
    try:
        # Esperar hasta que la pagina cargue
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        return driver

    except Exception as e:
        traceback.print_exception(e)
