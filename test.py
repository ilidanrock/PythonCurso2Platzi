def message_creator(text):
   # Escribe tu solución 👇

    response = {
        "computadora": "Con mi computadora puedo programar usando Python",
        "celular": "En mi celular puedo aprender usando la app de Platzi",
        "cable": "¡Hay un cable en mi bota!"
    }

    if text in response:
        # Hacer algo si la clave existe en el diccionario
        return (response[text])
    else:
        # Hacer algo si la clave no existe en el diccionario
        return ("Artículo no encontrado")


text = 'computadora'
response = message_creator(text)
print(response)
