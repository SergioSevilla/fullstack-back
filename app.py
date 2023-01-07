""" API Pizzas FullStack"""
from flask import Flask,request,redirect, Response
from persistencia import guardar_pedido

app = Flask(__name__)

@app.route("/pizza",methods=['POST'])
def registrar_pedido():
    """ Registramos los parámetros que nos vienen por POST de prepara_pedido. """
    nombre = request.form.get ("fname")
    apellidos = request.form.get ("surname")
    print("Nombre : "+nombre+" , Apellidos: "+apellidos)
    guardar_pedido(nombre,apellidos)
    return redirect("http://localhost/solicita_pedido.html", code=302)

@app.route("/checksize",methods=['POST'])
def checksize():
    """ Comprueba disponibilidad de un tamaño de pizza. """
    pizza_size = request.form.get ("size")
    if pizza_size == "S":
        mensaje = "No disponible"
    else:
        mensaje = "Disponible"
    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
