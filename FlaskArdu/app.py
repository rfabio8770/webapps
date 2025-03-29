from flask import Flask, render_template
from flask_socketio import SocketIO
import serial
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Configura el puerto serial (ajustar según el puerto de tu Arduino)
arduino = serial.Serial('COM4', 9600, timeout=1)  # En Linux/Mac puede ser '/dev/ttyUSB0'

def read_serial():
    """Función para leer datos del puerto serial y enviarlos vía WebSockets."""
    while True:
        if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').strip()
            if line:
                print("Recibido:", line)
                socketio.emit('data_update', {'message': line})

# Ejecuta la lectura en un hilo para no bloquear la app Flask
threading.Thread(target=read_serial, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')


