from scraper import scraper, get_categorias
from threading_scraper import thread_links


initial_url = "https://www.tiendasjumbo.co/supermercado"


def main():
    # Scraper de la pagina inicial
    page_categorias = scraper(initial_url)
    links_categorias = get_categorias(page_categorias)
    page_categorias.quit()
    thread_links(links_categorias)


if __name__ == "__main__":
    main()
