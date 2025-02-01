# create_db.py
import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('inventario.db')

# Crear un cursor
cursor = conn.cursor()

# Crear las tablas
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio REAL NOT NULL,
    cantidad INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS movimientos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto_id INTEGER NOT NULL,
    tipo TEXT NOT NULL,  -- 'ingreso' o 'egreso'
    cantidad INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY (producto_id) REFERENCES productos (id)
)
''')

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()
