from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
   # Lee un mensaje desde una variable de entorno, si existe, sino usa un default
   message = os.environ.get("APP_MESSAGE", "¡Hola desde mi contenedor Docker!")
   return f"<h1>{message}</h1>"

if __name__ == '__main__':
   # Escucha en todas las interfaces en el puerto 80
   # host='0.0.0.0' es importante para que sea accesible desde fuera del contenedor
   app.run(host='0.0.0.0', port=80)