import pymysql
import os 
from db import conectarMySQL, conectarRest
pymysql.cursors.DictCursor


def listarImagenes():
    conexion = conectarMySQL
    with conexion():
        urlFiles = 'static/uploads'
        return (os.listdir(urlFiles))

# def get_db_connection():
#     try:
#         connection = pymysql.connect(conectarRest())
#         print("Connected to MySQL database")
#         return connection
#     except pymysql.MySQLError as e:
#         print(f"Error while connecting to MySQL: {e}")
#         return None


#LOGIN
def login(email, password):
    conexion = conectarMySQL()
    try:
        with conexion.cursor() as cursor:
            sql = 'SELECT * FROM usuarios WHERE correo=%s AND contrasenia=%s'
            cursor.execute(sql, (email, password))
            result = cursor.fetchone()
            return result
    finally:
        conexion.close()

def loginAdm():
    conexion = conectarRest()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM restaurant_db_new")
            restaurants = cursor.fetchall()
        return restaurants
    finally:
        conexion.close()

#CRUD
def obtenerProductos():
    conexion = conectarMySQL()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM catalogo")
            catalogo = cursor.fetchall()
        return catalogo
    finally:
        conexion.close()

def cargarProducto(nombre, precio, imagen):
    conexion = conectarMySQL()
    try:
        with conexion.cursor() as cursor:
            query = "INSERT INTO catalogo (nombre, precio, imagen) VALUES (%s, %s, %s)"
            cursor.execute(query, (nombre, precio, imagen))
            conexion.commit()
            return cursor.lastrowid
    finally:
        conexion.close()

def obtener_prod_id(id):
    conexion = conectarMySQL()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM catalogo WHERE id = %s", (id,))
            prod = cursor.fetchone()
        return prod
    finally:
        conexion.close()

def actualizar_prod(nombre, precio, imagen, id):
    conexion = conectarMySQL()
    try:
        with conexion.cursor() as cursor:
            query = "UPDATE catalogo SET nombre=%s, precio=%s, imagen=%s WHERE id=%s"
            cursor.execute(query, (nombre, precio, imagen, id))
            conexion.commit()
            return cursor.rowcount
    finally:
        conexion.close()

def eliminar_prod(id):
    conexion = conectarMySQL()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM catalogo WHERE id = %s", (id,))
            conexion.commit()
            return cursor.rowcount
    finally:
        conexion.close()