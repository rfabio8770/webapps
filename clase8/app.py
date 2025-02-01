from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
# ruta para la página principal
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * from productos')
    productos = cursor.fetchall()
    conn.close()
    return render_template('productos.html', productos=productos)

@app.route('/producto/nuevo', methods=['GET', 'POST'])
def nuevo_producto():
    if request.method == "POST":
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()
        cursor.execute('''
                       INSERT INTO productos (nombre, descripcion, precio, cantidad)
                       VALUES (?, ?, ?, ?)''', (nombre, descripcion, precio, cantidad))
        conn.commit()
        conn.close()
        return redirect(url_for('productos'))
    return render_template('nuevo_producto.html')

# Ruta para registrar un movimiento
@app.route('/movimiento/nuevo', methods=['GET', 'POST'])
def nuevo_movimiento():
    if request.method == 'POST':
        producto_id = request.form['producto_id']
        tipo = request.form['tipo']
        cantidad = request.form['cantidad']
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO movimientos (producto_id, tipo, cantidad, fecha)
        VALUES (?, ?, ?, ?)
        ''', (producto_id, tipo, cantidad, fecha))
        
        conn.commit()
        conn.close()
        return redirect(url_for('movimientos'))
    
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    conn.close()
    return render_template('nuevo_movimiento.html', productos=productos)

# Ruta para mostrar los movimientos
@app.route('/movimientos')
def movimientos():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT movimientos.id, productos.nombre, movimientos.tipo, movimientos.cantidad, movimientos.fecha
    FROM movimientos
    JOIN productos ON movimientos.producto_id = productos.id
    ''')
    movimientos = cursor.fetchall()
    conn.close()
    return render_template('movimientos.html', movimientos=movimientos)