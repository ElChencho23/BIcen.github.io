import mysql.connector
from mysql.connector import Error
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static')

connection = None

def iniciar_conexion():
    try:
        global connection
        connection = mysql.connector.connect(
            host='localhost',
            database='hospital',
            user='root',
            password='JESUSdaniel444'
        )
        return True
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return False
    
def obtener_nombres_medicos():
    try:
        global connection
        cursor = connection.cursor()
        cursor.execute("SELECT nombre FROM medico;")
        resultados = cursor.fetchall()
        nombres = [fila[0] for fila in resultados]
        return nombres

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return []

@app.route("/")
def inicio():
    return render_template('index.html')

@app.route('/conexion', methods=['GET'])
def probar_conexion():
    bandera = iniciar_conexion()
    return jsonify({'Conexion': bandera})

@app.route('/medicos', methods=['GET'])
def get_medicos():
    nombres_medicos = obtener_nombres_medicos()
    print(nombres_medicos)
    return jsonify(nombres_medicos)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)