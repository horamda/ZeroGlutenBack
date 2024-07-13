from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
from os import remove, path
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL, MySQLdb
from datetime import date, datetime
from controller_db import *
from db import *
from models_form import db, Formulario  # Agregado para la integración de SQLAlchemy
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os

app = Flask(__name__)
app.secret_key = 'zerogluten789'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def basicInfo(getTitle):
    today = date.today()
    now = datetime.now()
    title = getTitle
    return [title, today.strftime('%Y'), now]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route("/")
def home():
    title = "Home"
    return render_template("index.html", title=basicInfo(title))

@app.route("/tiendas")
def cargarTienda():
    title = "Tienda"
    return render_template("tiendas.html", title=basicInfo(title))

@app.route("/congelados")
def cargarCongelados():
    productos = obtenerProductos()
    return render_template("congelados.html", productos=productos)

@app.route("/carrito")
def cargarCarrito():
    title = "Carrito"
    catalogo = obtenerProductos()
    return render_template("carrito.html", title=basicInfo(title), productos=catalogo)

@app.route("/preguntas_frecuentes")
def cargarPregfre():
    title = "Preguntas Frecuentes"
    return render_template("preguntas_frecuentes.html", title=basicInfo(title))

@app.route("/contacto")
def cargarContacto():
    title = "Contacto"
    return render_template("contacto.html", title=basicInfo(title))

@app.route("/loginAdm")
def Acc_Adm():
    title = "Iniciar Sesion"
    return render_template("/login.html", title=basicInfo(title))

@app.route("/acceso-usuario", methods=['POST'])
def ingresa_datos():
    email = request.form['email']
    password = request.form['password']
    usuario = login(email, password)
    if usuario:
        session['loggedin'] = True
        session['correo'] = usuario['correo']
        flash('¡Inicio de sesión exitoso!', 'success')
        return redirect("/paneladm")
    else:
        flash('¡Correo o contraseña incorrectos!', 'danger')
        return redirect("/login")

@app.route("/paneladm")
def Adm_Op():
    title = "Panel de Administrador"
    return render_template("/paneladm.html", title=basicInfo(title))


@app.route("/administrador")
def Admin():
    title = "Catalogo"
    if 'loggedin' in session:
        catalogo = obtenerProductos()
        return render_template("administrador.html", title=basicInfo(title), productos=catalogo)
    else:
        return redirect("/login")

@app.route("/cargar_prod", methods=['GET', 'POST'])
def cargar_nuevo_producto():
    title = "Nuevo Producto"
    if request.method == 'POST':
        if 'imagen' not in request.files:
            flash('No se ha seleccionado ninguna imagen.', 'danger')
            return redirect(request.url)

        file = request.files['imagen']
        if file.filename == '':
            flash('No se ha seleccionado ninguna imagen.', 'danger')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            nom_prod = request.form['nombre']
            pre_prod = request.form['precio']
            img_prod = filename

            result = cargarProducto(nom_prod, pre_prod, img_prod)
            if result:
                flash('Producto agregado con éxito.', 'success')
            else:
                flash('Hubo un error al agregar el producto.', 'danger')
            return redirect('/administrador')

    return render_template('nuevo_prod.html', title=basicInfo(title))

@app.route("/editar_prod/<int:id>", methods=['GET', 'POST'])
def editarProd(id):
    title = "Editar Producto"
    if request.method == 'POST':
        nom_edit = request.form['prod_nombre']
        pre_edit = request.form['prod_precio']
        img_actual = request.form['prod_imagen_actual']

        if 'prod_imagen' in request.files:
            file = request.files['prod_imagen']
            if file and file.filename != '':
                if allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(filepath)
                    img_edit = filename
                else:
                    flash('Tipo de archivo no permitido', 'danger')
                    return redirect(request.url)
            else:
                img_edit = img_actual
        else:
            img_edit = img_actual

        actualizar_prod(nom_edit, pre_edit, img_edit, id)
        flash('Producto actualizado con éxito.', 'success')
        return redirect('/administrador')
    else:
        producto = obtener_prod_id(id)
        return render_template('editar_prod.html', title=title, producto=producto)

@app.route("/borrar_prod/<int:id>")
def borrarProd(id):
    eliminar_prod(id)
    return redirect("/administrador")



@app.route('/buscar_producto', methods=['GET'])
def buscar_producto():
    query = request.args.get('query', '')
    conexion = conectarMySQL()
    try:
        with conexion.cursor() as cursor:
            query_sql = "SELECT id, nombre, precio, imagen FROM catalogo WHERE nombre LIKE %s OR precio LIKE %s"
            cursor.execute(query_sql, (f'%{query}%', f'%{query}%'))
            productos = cursor.fetchall()
        return jsonify(productos)
    finally:
        conexion.close()

@app.route('/add_restaurant', methods=['GET', 'POST'])
def add_restaurant():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        province = request.form['province']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        phone = request.form['phone']
        website = request.form['website']
        image = None

        if 'image' in request.files:
            file = request.files['image']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image = filename
        
        conn = conectarRest() 
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO restaurants (name, address, province, latitude, longitude, phone, website, image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                               (name, address, province, latitude, longitude, phone, website, image))
                conn.commit()
                cursor.close()
            except pymysql.MySQLError as e:
                print(f"Error executing query: {e}")
            finally:
                conn.close()
            return redirect('/restaurants')
        else:
            return "Error connecting to the database"
    return render_template('add_restaurant.html')

@app.route('/edit_restaurant/<int:id>', methods=['GET', 'POST'])
def edit_restaurant(id):
    conn = conectarRest()
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        province = request.form['province']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        phone = request.form['phone']
        website = request.form['website']
        image = request.form.get('existing_image')
        
        if 'image' in request.files:
            file = request.files['image']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image = filename

        try:
            cursor = conn.cursor()
            cursor.execute('UPDATE restaurants SET name=%s, address=%s, province=%s, latitude=%s, longitude=%s, phone=%s, website=%s, image=%s WHERE id=%s',
                           (name, address, province, latitude, longitude, phone, website, image, id))
            conn.commit()
            cursor.close()
        except pymysql.MySQLError as e:
            print(f"Error executing query: {e}")
        finally:
            conn.close()
        return redirect('/restaurants')
    else:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM restaurants WHERE id = %s', (id,))
            restaurant = cursor.fetchone()
            cursor.close()
        except pymysql.MySQLError as e:
            print(f"Error executing query: {e}")
        return render_template('edit_restaurant.html', restaurant=restaurant)
  
    
    
@app.route('/delete_restaurant/<int:id>', methods=['POST'])
def delete_restaurant(id):
    conn = conectarRest()
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM restaurants WHERE id = %s', (id,))
        conn.commit()
        cursor.close()
    except pymysql.MySQLError as e:
        print(f"Error executing query: {e}")
    finally:
        conn.close()
    return redirect('/restaurants')

@app.route('/restaurants')
def restaurants():
    conn = conectarRest()
    if conn:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM restaurants')
        restaurants = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('restaurants.html', restaurants=restaurants)
    else:
        return render_template('error.html', error_message="Error connecting to the database")

@app.route('/restaurantes')
def mostrar_restaurantes():
    conn = conectarRest()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT name, address, phone, website, province, image FROM restaurants')
        restaurantes = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('restaurantes.html', restaurantes=restaurantes)
    else:
        return render_template('error.html', error_message="Error connecting to the database")
    
    
    
@app.route('/contactoABM', methods=['GET'])
def contactoABM():
    conn = conectarRest()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, nombre, email, motivo_contacto, serv_utilizado, ubicacion, mensaje, newsletter, leido FROM formulario')
        contactos = cursor.fetchall()
        cursor.close()
        conn.close()
        title = "Envíos de Formulario de Contacto"
        return render_template('contactoABM.html', contact_forms=contactos, title=title)
    else:
        return render_template('error.html', error_message="Error connecting to the database")

@app.route('/contactoABM/<int:id>', methods=['GET'])
def ver_contacto(id):
    conn = conectarRest()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, nombre, email, motivo_contacto, serv_utilizado, ubicacion, mensaje, newsletter, leido FROM formulario WHERE id = %s', (id,))
        contacto = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('ver_contacto.html', contact_form=contacto)
    else:
        return render_template('error.html', error_message="Error connecting to the database")

@app.route('/contactoABM/<int:id>/editar', methods=['GET', 'POST'])
def editar_contacto(id):
    conn = conectarRest()
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        motivo_contacto = request.form['motivo_contacto']
        serv_utilizado = request.form['serv_utilizado']
        ubicacion = request.form['ubicacion']
        mensaje = request.form['mensaje']
        newsletter = 'Sí' if 'newsletter' in request.form else 'No'
        leido = 'leido' in request.form

        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE formulario
                SET nombre = %s, email = %s, motivo_contacto = %s, serv_utilizado = %s, ubicacion = %s, mensaje = %s, newsletter = %s, leido = %s
                WHERE id = %s
            """, (nombre, email, motivo_contacto, serv_utilizado, ubicacion, mensaje, newsletter, leido, id))
            conn.commit()
            cursor.close()
            conn.close()
            flash('Contacto actualizado correctamente.', 'success')
            return redirect(url_for('contactoABM'))
        else:
            return render_template('error.html', error_message="Error connecting to the database")

    else:
        if conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, nombre, email, motivo_contacto, serv_utilizado, ubicacion, mensaje, newsletter, leido FROM formulario WHERE id = %s', (id,))
            contacto = cursor.fetchone()
            cursor.close()
            conn.close()
            return render_template('editar_contacto.html', contacto=contacto)
        else:
            return render_template('error.html', error_message="Error connecting to the database")

@app.route('/contactoABM/<int:id>/eliminar', methods=['POST'])
def eliminar_contacto(id):
    conn = conectarRest()
    if conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM formulario WHERE id = %s', (id,))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Contacto eliminado correctamente.')
        return redirect(url_for('contactoABM'))
    else:
        return render_template('error.html', error_message="Error connecting to the database")

@app.route('/filtrarContacto', methods=['GET', 'POST'])
def filtrarContacto():
    estado = request.args.get('estado', 'todos')
    conn = conectarRest()
    if conn:
        cursor = conn.cursor()
        if estado == 'Leidos':
            cursor.execute('SELECT id, nombre, email, motivo_contacto, serv_utilizado, ubicacion, mensaje, newsletter, leido FROM formulario WHERE leido = TRUE')
        elif estado == 'No_leidos':
            cursor.execute('SELECT id, nombre, email, motivo_contacto, serv_utilizado, ubicacion, mensaje, newsletter, leido FROM formulario WHERE leido = FALSE')
        else:
            cursor.execute('SELECT id, nombre, email, motivo_contacto, serv_utilizado, ubicacion, mensaje, newsletter, leido FROM formulario')
        contactos = cursor.fetchall()
        cursor.close()
        conn.close()
        title = "Envíos de Formulario de Contacto"
        return render_template('contactoABM.html', contact_forms=contactos, title=title)
    else:
        return render_template('error.html', error_message="Error connecting to the database")


    

if __name__ == '__main__':
    app.run(debug=True)
