from flask import Flask,request,redirect
from persistencia import guardar_pedido

app = Flask(__name__)

@app.route("/pizza",methods=['POST'])
#Registramos los parámetros que nos vienen por POST de prepara_pedido. 
def registrar_pedido():
  nombre = request.form.get ("fname")
  apellidos = request.form.get ("surname")
  print("Nombre : "+nombre+" , Apellidos: "+apellidos)
  guardar_pedido(nombre,apellidos)
  return redirect("http://localhost/solicita_pedido.html", code=302) 