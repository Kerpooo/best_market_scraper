import threading
from in_page_scripts import go_to_page
from scraper import (
    scraper,
    get_cantidad_paginas,
    get_productos,
    get_productos_data,
)


def thread_links(links: list[str]):
    # Pasa por cada una de las categorias
    for i in range(1, len(links)):
        # Se hace la peticion de la pagina de esa categoria
        categoria = scraper(links[i])
        # Obtiene numero de paginas de esa categoria
        numero_de_paginas = get_cantidad_paginas(categoria)
        # Se itera por cada pagina
        for pagina in range(2, numero_de_paginas):
            # Se obtiene una lista de los productos de la pagina en la que se esta
            productos_list = get_productos(categoria)
            # Se obtienen caracteristicas de cada uno de los productos
            print(get_productos_data(productos_list))
            # Va a la pagina que se recibe como parametro, es decir la siguiente
            go_to_page(categoria, pagina)
            # Cuando se llega a la ultima pagina este vuelve a hacer la obtencion
            if pagina == numero_de_paginas - 1:
                productos_list = get_productos(categoria)
                print(get_productos_data(productos_list))
