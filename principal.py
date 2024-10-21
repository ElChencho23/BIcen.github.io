import mysql.connector
from mysql.connector import Error
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static')

connection = None

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='hospital',
        user='root',
        password='JESUSdaniel444'
    )
    connection.autocommit = True
except Error as e:
    print(f"Error al conectar a MySQL: {e}")

def insertar_historial(edad, motivo_consulta, padecimiento_actual, resultado_laboratorio, diagnosticos, tratamiento,
                       interrogatorio, curp_persona, cedula_medico):
    try:
        global connection
        cursor = connection.cursor()
        
        params = [edad, motivo_consulta, padecimiento_actual, resultado_laboratorio, 
                diagnosticos, tratamiento, interrogatorio, curp_persona, cedula_medico, 0]

        cursor.callproc('InsertarHistorialClinico', params)

        id_generado = params[9]
        
        return id_generado
    except Error as e:
        print(e)
        return -1

def insertar_persona(curp, nombre, fecha_nacimiento, grupo_sanguineo, jurisdiccion, escolaridad,
                     edad, sexo, estado_civil, ocupacion, tipo_seguro, calle, num,
                     colonia, municipio, lugar_procedencia, telefono, ageb, alergia,
                     tipo_alergia, id_unidad_medica):
    try:
        global connection
        cursor = connection.cursor()
        
        # Definir los parámetros para el procedimiento almacenado
        params = [curp, nombre, fecha_nacimiento, grupo_sanguineo, jurisdiccion, escolaridad,
                  edad, sexo, estado_civil, ocupacion, tipo_seguro, calle, num,
                  colonia, municipio, lugar_procedencia, telefono, ageb, alergia,
                  tipo_alergia, id_unidad_medica]

        cursor.callproc('InsertarPersona', params)

        return True
    except Error as e:
        print(e)
        return False


@app.route("/")
def inicio():
    return render_template('index.html')

@app.route('/Insertar_historial_medico', methods=['POST'])
def insertar_historial_medico():
    
    data = request.get_json()
    
    edad = data.get('edad')
    motivo_consulta = data.get('motivo_consulta')
    padecimiento_actual = data.get('padecimiento_actual')
    resultado_laboratorio = data.get('resultado_laboratorio')
    diagnosticos = data.get('diagnosticos')
    tratamiento = data.get('tratamiento')
    interrogatorio = data.get('interrogatorio')
    curp_persona = data.get('curp_persona')
    cedula_medico = data.get('cedula_medico')
    
    id_historial = insertar_historial(edad, motivo_consulta, padecimiento_actual, resultado_laboratorio,
                                      diagnosticos, tratamiento, interrogatorio, curp_persona, cedula_medico)
    
    estatus = False
    
    if id_historial > 0:
        estatus = True
    
    return jsonify({
        'Estado' : estatus,
        'ID' : id_historial
    })
    
@app.route('/Insertar_persona', methods=['POST'])
def insertar_persona():
    
    data = request.get_json()
    
    curp = data.get('curp')
    nombre = data.get('nombre')
    fecha_nacimiento = data.get('fecha_nacimiento')
    grupo_sanguineo = data.get('grupo_sanguineo')
    jurisdiccion = data.get('jurisdiccion')
    escolaridad = data.get('escolaridad')
    edad = data.get('edad')
    sexo = data.get('sexo')
    estado_civil = data.get('estado_civil')
    ocupacion = data.get('ocupacion')
    tipo_seguro = data.get('tipo_seguro')
    calle = data.get('calle')
    num = data.get('num')
    colonia = data.get('colonia')
    municipio = data.get('municipio')
    lugar_procedencia = data.get('lugar_procedencia')
    telefono = data.get('telefono')
    ageb = data.get('ageb')
    alergia = data.get('alergia')
    tipo_alergia = data.get('tipo_alergia')
    id_unidad_medica = data.get('id_unidad_medica')

    
    id_historial = insertar_historial(edad, motivo_consulta, padecimiento_actual, resultado_laboratorio,
                                      diagnosticos, tratamiento, interrogatorio, curp_persona, cedula_medico)
    
    estatus = False
    
    if id_historial > 0:
        estatus = True
    
    return jsonify({
        'Estado' : estatus,
        'ID' : id_historial
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)