""" Persistencia de Pizza Full Stack"""

def guardar_pedido(nombre, apellidos):
    """ Abre el fichero pedidos.txt para agregar la dupla <nombre,apellidos> como un pedido. """
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(nombre + " " + apellidos + "\n")             #Cada línea será un pedido.
        file.close()
