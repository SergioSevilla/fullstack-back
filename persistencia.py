def guardar_pedido(nombre, apellidos):
  ''' Abre el fichero pedidos.txt en modo append para agregar la 
      dupla <nombre,apellidos> como un pedido. Una vez escrito en 
      el fichero, se cierra. '''
      
  with open("pedidos.txt", "a", encoding="utf-8") as file:  
    file.write(nombre + " " + apellidos + "\n")             #Cada línea será un pedido.
    file.close()