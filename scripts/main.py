# Importamos los otros módulos
import librerias
import configuracion
import inputs_usuario
import funciones


# Iniciamos el diccionario
diccionario_castellano = configuracion.ruta_diccionario

# Iniciamos los inputs del usuario
lista_letras_contiene = inputs_usuario.letras_contiene
lista_letras_no_contiene = inputs_usuario.letras_no_contiene
rango = inputs_usuario.rango_longitud
tildes = inputs_usuario.considerar_tildes
lista_empieza_por = inputs_usuario.lista_empieza_por
lista_termina_por = inputs_usuario.lista_termina_por
lista_contiene_cadena = inputs_usuario.lista_contiene_cadena
lista_no_contiene_cadena = inputs_usuario.lista_no_contiene_cadena

# Ejecutamos función principal
palabras_filtradas = funciones.filtrar_palabras(diccionario_castellano, lista_letras_contiene, lista_letras_no_contiene, rango, tildes, lista_empieza_por, lista_termina_por, lista_contiene_cadena, lista_no_contiene_cadena)

# Printeamos resultados en terminal
funciones.resultados(palabras_filtradas)
