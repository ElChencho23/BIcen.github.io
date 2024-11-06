import mysql.connector
from mysql.connector import Error
from flask import Flask, render_template, request, jsonify
from datetime import datetime

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

def insertar_historial_clinico(edad, motivo_consulta, padecimiento_actual, resultado_laboratorio, diagnosticos, tratamiento, fecha, interrogatorio, curp_persona, cedula_medico):
    try:
        cursor = connection.cursor()
            
        sql = "CALL InsertarHistorialClinico(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, @id)"
        val = (edad, motivo_consulta, padecimiento_actual, resultado_laboratorio, 
            diagnosticos, tratamiento, fecha, interrogatorio, curp_persona, cedula_medico)
        cursor.execute(sql, val)
            
        cursor.execute("SELECT @id")
        result = cursor.fetchone()
        id_insertado = result[0]

        print("ID insertado:", id_insertado)

        return id_insertado 

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return -1

def insertar_antecedentes_familiares(diabetes, hta, oncologicos, couagulopatias, alta_genetica, vih_sida, 
                                    tuberculosis, alergia, cardiopatias, obesidad, artritis, hemofilia, 
                                    mentales, toxicomanias, alcoholismo, hiperlipidemias, otro, id_historial_clinico):
    try:
        # Crear un cursor para ejecutar el procedimiento almacenado
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado con los parámetros correspondientes
        sql = """CALL InsertarAntecedentesFamiliares(
                    %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, @success)"""
        
        # Parámetros para la ejecución del procedimiento
        val = (diabetes, hta, oncologicos, couagulopatias, alta_genetica, vih_sida, 
               tuberculosis, alergia, cardiopatias, obesidad, artritis, hemofilia, 
               mentales, toxicomanias, alcoholismo, hiperlipidemias, otro, id_historial_clinico)

        # Ejecutar el procedimiento
        cursor.execute(sql, val)

        # Obtener el valor del parámetro de salida @success
        cursor.execute("SELECT @success")
        result = cursor.fetchone()
        success = result[0]

        if success:
            print("Inserción exitosa")
        else:
            print("Error al insertar los antecedentes familiares")

        return success

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return False
    
def insertar_antecedentes_no_patologicos(alimentacion, cantidad_alimentacion, fecuencia_alimentacion, habitos_higiene, 
                                         alcoholismo, frecuencia_alcoholismo, tabaquismo, numero_cigarros, drogas, 
                                         tipo_drogas, inmunizaciones, tipo_inmunizaciones, id_historial_clinico):
    try:
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado con los parámetros correspondientes
        sql = """CALL InsertarAntecedentesNoPatologicos(
                    %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, 
                    %s, @success)"""
        
        # Parámetros para la ejecución del procedimiento
        val = (alimentacion, cantidad_alimentacion, fecuencia_alimentacion, habitos_higiene, alcoholismo, 
               frecuencia_alcoholismo, tabaquismo, numero_cigarros, drogas, tipo_drogas, inmunizaciones, 
               tipo_inmunizaciones, id_historial_clinico)

        # Ejecutar el procedimiento
        cursor.execute(sql, val)

        # Obtener el valor del parámetro de salida @success
        cursor.execute("SELECT @success")
        result = cursor.fetchone()
        success = result[0]

        if success:
            print("Inserción exitosa")
        else:
            print("Error al insertar los antecedentes no patológicos")

        # Cerrar el cursor
        cursor.close()
        return success

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return False
    
def insertar_antecedentes_personales_patologicos(alergia, reumatismo, diabetes, hipertensivo, its, vih_sida, 
                                                neurologico, infeccion, parasito_intestinal, quirurgico, 
                                                hemotransfusion, cardiopatias, enf_renal, cancer, anemia, 
                                                hemorragias, hepatitis, neumopatias, paludismo, fibre_tifoidea, 
                                                brucelosis, crisis_convulsivas, enf_mental, traumatico, ulcera, 
                                                medicamento_actual, otras_patologias, id_historial_clinico):
    try:
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado con los parámetros correspondientes
        sql = """CALL InsertarAntecedentesPersonalesPatologicos(
                    %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, @success)"""
        
        # Parámetros para la ejecución del procedimiento
        val = (alergia, reumatismo, diabetes, hipertensivo, its, vih_sida, 
               neurologico, infeccion, parasito_intestinal, quirurgico, hemotransfusion, 
               cardiopatias, enf_renal, cancer, anemia, hemorragias, hepatitis, neumopatias, 
               paludismo, fibre_tifoidea, brucelosis, crisis_convulsivas, enf_mental, traumatico, 
               ulcera, medicamento_actual, otras_patologias, id_historial_clinico)

        # Ejecutar el procedimiento
        cursor.execute(sql, val)

        # Obtener el valor del parámetro de salida @success
        cursor.execute("SELECT @success")
        result = cursor.fetchone()
        success = result[0]

        if success:
            print("Inserción exitosa")
        else:
            print("Error al insertar los antecedentes personales patológicos")

        # Cerrar el cursor
        cursor.close()
        return success

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return False
    
def insertar_antecedentes_gineco_obstetricos(menarca, ritmo, ivsa, cs, mp_f, gesta, para, cesarea, aborto, fum, doc, 
                                            docma, antecedentes_peritenales, id_historial_clinico):
    try:
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado con los parámetros correspondientes
        sql = """CALL InsertarAntecedentesGinecoObstetricos(
                    %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, 
                    %s, %s, @success)"""
        
        # Parámetros para la ejecución del procedimiento
        val = (menarca, ritmo, ivsa, cs, mp_f, gesta, para, cesarea, aborto, fum, doc, docma, antecedentes_peritenales, id_historial_clinico)

        # Ejecutar el procedimiento
        cursor.execute(sql, val)

        # Obtener el valor del parámetro de salida @success
        cursor.execute("SELECT @success")
        result = cursor.fetchone()
        success = result[0]

        if success:
            print("Inserción exitosa")
        else:
            print("Error al insertar los antecedentes gineco-obstétricos")

        # Cerrar el cursor
        cursor.close()
        return success

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return False
    
def insertar_interrogatorio_aparato_sistema(sistomas_generales, respiratorio, digestivo, nervioso, musculoesqueletico, cardiovascular,
                                            genitourinario, endoctrico, psiquico, piel_mucosa, organos_sentidos, hematico_linfatico,
                                            cabeza_cuello, organos_reproductivos, id_historial_clinico):
    try:
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado con los parámetros correspondientes
        sql = """CALL InsertarInterrogatorioAparatoSistema(
                    %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, @success)"""
        
        # Parámetros para la ejecución del procedimiento
        val = (sistomas_generales, respiratorio, digestivo, nervioso, musculoesqueletico, cardiovascular,
               genitourinario, endoctrico, psiquico, piel_mucosa, organos_sentidos, hematico_linfatico,
               cabeza_cuello, organos_reproductivos, id_historial_clinico)

        # Ejecutar el procedimiento
        cursor.execute(sql, val)

        # Obtener el valor del parámetro de salida @success
        cursor.execute("SELECT @success")
        result = cursor.fetchone()
        success = result[0]

        if success:
            print("Inserción exitosa")
        else:
            print("Error al insertar el interrogatorio de aparato sistema")

        # Cerrar el cursor
        cursor.close()
        return success

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return False
    
def insertar_exploracion_fisica(pulso, temperatura, tension_arterial, frecuencia_cardiaca, frecuencia_respiratoria,
                                cabeza, cuello, torax, abdomen, miembros, genitales, id_historial_clinico):
    try:
        cursor = connection.cursor()

        # Llamar al procedimiento almacenado con los parámetros correspondientes
        sql = """CALL InsertarExploracionFisica(
                    %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, @success)"""
        
        # Parámetros para la ejecución del procedimiento
        val = (pulso, temperatura, tension_arterial, frecuencia_cardiaca, frecuencia_respiratoria,
               cabeza, cuello, torax, abdomen, miembros, genitales, id_historial_clinico)

        # Ejecutar el procedimiento
        cursor.execute(sql, val)

        # Obtener el valor del parámetro de salida @success
        cursor.execute("SELECT @success")
        result = cursor.fetchone()
        success = result[0]

        if success:
            print("Inserción exitosa")
        else:
            print("Error al insertar la exploración física")

        # Cerrar el cursor
        cursor.close()
        return success

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return False

@app.route("/")
def inicio():
    return render_template('index.html')

@app.route('/Insertar_historial_medico', methods=['POST'])
def insertar_historial_medico():
    
    edad = 45
    motivo_consulta = "Dolor de cabeza persistente"
    padecimiento_actual = "Paciente refiere dolor constante en la zona frontal desde hace 3 días"
    resultado_laboratorio = "Hemoglobina en niveles normales, colesterol alto"
    diagnosticos = "Migraña con aura, hipercolesterolemia"
    fecha_actual = datetime.now()
    tratamiento = "Paracetamol 500 mg cada 8 horas, dieta baja en grasas"
    interrogatorio = True
    curp_persona = "ABC1234567890XYZ"
    cedula_medico = "MED123456"
    '''
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
    '''
    id_historial = insertar_historial_clinico(edad, motivo_consulta, padecimiento_actual, resultado_laboratorio,
                                      diagnosticos, tratamiento, fecha_actual, interrogatorio, curp_persona, cedula_medico)
    
    estatus = False
    id = int(id_historial)
    
    if id > 0:
        estatus = True
    print(id)
    if id < 0:
        return jsonify({
            'Estado' : False,
            'ID' : -1,
            'Problema': 'Error al insetar un dato en la tabla Historial_clinico'
        })
    diabetes = 'Sí'
    hta = 'No'
    oncologicos = 'No'
    couagulopatias = 'No'
    alta_genetica = 'No'
    vih_sida = True
    tuberculosis = 'No'
    alergia = 'No'
    cardiopatias = 'Sí'
    obesidad = 'No'
    artritis = 'Sí'
    hemofilia = 'No'
    mentales = 'No'
    toxicomanias = 'No'
    alcoholismo = 'No'
    hiperlipidemias = 'No'
    otro = 'Ninguno'

    success = insertar_antecedentes_familiares(
        diabetes, hta, oncologicos, couagulopatias, alta_genetica, vih_sida, 
        tuberculosis, alergia, cardiopatias, obesidad, artritis, hemofilia, 
        mentales, toxicomanias, alcoholismo, hiperlipidemias, otro, id
    )
    print(f'Insertar datos de antecedentes familiares {success}')
    
    alimentacion = 'Saludable'
    cantidad_alimentacion = 'Normal'
    fecuencia_alimentacion = 3  # Comer 3 veces al día
    habitos_higiene = 'Buena higiene'
    alcoholismo = 'No'
    frecuencia_alcoholismo = 'Nunca'
    tabaquismo = 'No'
    numero_cigarros = '0'
    drogas = 'No'
    tipo_drogas = 'Ninguno'
    inmunizaciones = True
    tipo_inmunizaciones = 'Vacunas básicas'

    # Llamada de ejemplo para insertar antecedentes no patológicos
    success_antecedentes_no_patologicos = insertar_antecedentes_no_patologicos(
        alimentacion, cantidad_alimentacion, fecuencia_alimentacion, habitos_higiene, alcoholismo, 
        frecuencia_alcoholismo, tabaquismo, numero_cigarros, drogas, tipo_drogas, inmunizaciones, 
        tipo_inmunizaciones, id
    )
    
    print(f'antecedentes no patologicos {success_antecedentes_no_patologicos}')
    
    alergia = 'No'
    reumatismo = 'No'
    diabetes = 'Sí'
    hipertensivo = 'No'
    its = 'No'
    vih_sida = 'No'
    neurologico = 'Ninguno'
    infeccion = 'No'
    parasito_intestinal = 'Ninguno'
    quirurgico = 'No'
    hemotransfusion = 'No'
    cardiopatias = 'No'
    enf_renal = 'No'
    cancer = 'No'
    anemia = 'No'
    hemorragias = 'No'
    hepatitis = 'No'
    neumopatias = 'No'
    paludismo = 'No'
    fibre_tifoidea = 'No'
    brucelosis = 'No'
    crisis_convulsivas = 'No'
    enf_mental = 'No'
    traumatico = 'No'
    ulcera = 'No'
    medicamento_actual = 'No'
    otras_patologias = 'Ninguna'

    # Llamada de ejemplo para insertar antecedentes personales patológicos
    success_antecedentes_personales_patologicos = insertar_antecedentes_personales_patologicos(
        alergia, reumatismo, diabetes, hipertensivo, its, vih_sida, neurologico, infeccion, parasito_intestinal, 
        quirurgico, hemotransfusion, cardiopatias, enf_renal, cancer, anemia, hemorragias, hepatitis, neumopatias, 
        paludismo, fibre_tifoidea, brucelosis, crisis_convulsivas, enf_mental, traumatico, ulcera, medicamento_actual, 
        otras_patologias, id
    )
    
    print('antecedentes personales patologicos ',success_antecedentes_personales_patologicos)
    
    menarca = '13 años'
    ritmo = 'Regular'
    ivsa = 'Si'
    cs = 'No'
    mp_f = 'No'
    gesta = '2'
    para = '2'
    cesarea = 'No'
    aborto = '1'
    fum = '2023-09-01'
    doc = 'No'
    docma = 'No'
    antecedentes_peritenales = 'Ninguno'

    # Llamada de ejemplo para insertar antecedentes gineco-obstétricos
    success_antecedentes_gineco = insertar_antecedentes_gineco_obstetricos(
        menarca, ritmo, ivsa, cs, mp_f, gesta, para, cesarea, aborto, fum, doc, docma, antecedentes_peritenales, id
    )
    print('gineco ', success_antecedentes_gineco)
    
    sistomas_generales = 'Sin fiebre ni dolor'
    respiratorio = 'No presenta dificultad respiratoria'
    digestivo = 'Normal'
    nervioso = 'Sin alteraciones'
    musculoesqueletico = 'Dolor en rodilla'
    cardiovascular = 'Sin problemas de circulación'
    genitourinario = 'Normal'
    endoctrico = 'Sin alteraciones hormonales'
    psiquico = 'Estable'
    piel_mucosa = 'Sin lesiones'
    organos_sentidos = 'Normal'
    hematico_linfatico = 'Normal'
    cabeza_cuello = 'Sin problemas'
    organos_reproductivos = 'Normal'

    # Llamada de ejemplo para insertar interrogatorio aparato-sistema
    success_aparato = insertar_interrogatorio_aparato_sistema(
        sistomas_generales, respiratorio, digestivo, nervioso, musculoesqueletico, cardiovascular,
        genitourinario, endoctrico, psiquico, piel_mucosa, organos_sentidos, hematico_linfatico,
        cabeza_cuello, organos_reproductivos, id
    )
    print('aparato ',success_aparato)
    
    pulso = 72.0
    temperatura = 36.6
    tension_arterial = 120.80
    frecuencia_cardiaca = 72.0
    frecuencia_respiratoria = 16.0
    cabeza = 'Sin alteraciones'
    cuello = 'Normal'
    torax = 'Sin lesiones'
    abdomen = 'Abdomen plano y no doloroso'
    miembros = 'Sin edema ni deformidades'
    genitales = 'Normales'
    id_historial_clinico = 123  # Este es el ID del historial clínico del paciente

    # Llamada de ejemplo para insertar exploración física
    success_exploracion = insertar_exploracion_fisica(
        pulso, temperatura, tension_arterial, frecuencia_cardiaca, frecuencia_respiratoria,
        cabeza, cuello, torax, abdomen, miembros, genitales, id_historial_clinico
    )
    
    print('exploracion fisica ', success_exploracion)
    
    return jsonify({
        'Estado' : estatus,
        'ID' : id
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