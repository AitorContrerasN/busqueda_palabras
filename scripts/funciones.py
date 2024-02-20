import librerias

def normalizar_palabra(palabra, considerar_tildes=True):
    """
    Normaliza las palabras eliminando las tildes si se indica.

    :param palabra: La palabra a normalizar.
    :param considerar_tildes: Si es False, elimina las tildes de la palabra.
    :return: Palabra normalizada.
    """
    if not considerar_tildes:
        return ''.join(c for c in librerias.unicodedata.normalize('NFD', palabra) if librerias.unicodedata.category(c) != 'Mn')
    return palabra

def filtrar_palabras(archivo_dict, letras_incluir, letras_excluir, rango_longitud, considerar_tildes=True, lista_empieza_por=None, lista_termina_por=None, lista_contiene_cadena=None, lista_no_contiene_cadena=None):
    """
    Filtra las palabras de un archivo de texto según varios criterios.

    :param archivo_dict: Ruta al archivo de texto con el diccionario, una palabra por línea.
    :param letras_incluir: Lista de letras que deben estar en las palabras.
    :param letras_excluir: Lista de letras que no deben estar en las palabras.
    :param rango_longitud: Lista con el número mínimo y máximo de caracteres permitidos en las palabras. Si está vacía, no se aplica esta condición.
    :param considerar_tildes: Indica si se deben considerar las tildes.
    :param lista_empieza_por: Lista de cadenas por las cuales debe empezar la palabra. Si está vacía, no se aplica esta condición.
    :param lista_termina_por: Lista de cadenas por las cuales debe terminar la palabra. Si está vacía, no se aplica esta condición.
    :param lista_contiene_cadena: Lista de cadenas que deben estar contenidas en la palabra. Si está vacía, no se aplica esta condición.
    :param lista_no_contiene_cadena: Lista de cadenas que no deben estar contenidas en la palabra. Si está vacía, no se aplica esta condición.
    :return: Lista de palabras filtradas.
    """
    palabras_filtradas = []

    with open(archivo_dict, 'r', encoding='utf-8') as archivo:
        for palabra in archivo:
            palabra = palabra.strip()  # Elimina espacios y saltos de línea
            palabra_normalizada = normalizar_palabra(palabra, considerar_tildes)
            
            # Condición de longitud
            if rango_longitud:
                min_longitud, max_longitud = rango_longitud
                if not (min_longitud <= len(palabra_normalizada) <= max_longitud):
                    continue
            
            # Condición de letras a incluir
            if letras_incluir and not all(letra in palabra_normalizada for letra in letras_incluir):
                continue
            
            # Condición de letras a excluir
            if letras_excluir and any(letra in palabra_normalizada for letra in letras_excluir):
                continue
            
            # Condición de inicio de palabra
            if lista_empieza_por and not any(palabra_normalizada.startswith(prefijo) for prefijo in lista_empieza_por):
                continue
            
            # Condición de fin de palabra
            if lista_termina_por and not any(palabra_normalizada.endswith(sufijo) for sufijo in lista_termina_por):
                continue
            
            # Condición de contención de cadena
            if lista_contiene_cadena and not any(cadena in palabra_normalizada for cadena in lista_contiene_cadena):
                continue
            
            # Condición de no contención de cadena
            if lista_no_contiene_cadena and any(cadena in palabra_normalizada for cadena in lista_no_contiene_cadena):
                continue
            
            palabras_filtradas.append(palabra)
    
    return palabras_filtradas

def resultados(lista): 
    longitud = len(lista)
    print(f'Resultado: {longitud} palabras')
    print('--------')
    for i in lista: 
        print(i)