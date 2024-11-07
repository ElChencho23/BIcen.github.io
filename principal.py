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
    
def actualizar_historial_clinico(id_historial, edad, motivo_consulta, padecimiento_actual, resultado_laboratorio, 
                                diagnosticos, tratamiento, fecha, interrogatorio, curp_persona, cedula_medico):
    try:
        cursor = connection.cursor()

        # Llamada al procedimiento almacenado
        sql = """CALL ActualizarHistorialClinico(
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, @success)"""
        
        # Parámetros para la ejecución del procedimiento
        val = (id_historial, edad, motivo_consulta, padecimiento_actual, resultado_laboratorio, 
               diagnosticos, tratamiento, fecha, interrogatorio, curp_persona, cedula_medico)

        # Ejecutar el procedimiento
        cursor.execute(sql, val)

        # Obtener el valor del parámetro de salida @success
        cursor.execute("SELECT @success")
        result = cursor.fetchone()
        success = result[0]

        if success:
            print("Actualización exitosa")
        else:
            print("Error al actualizar el historial clínico")

        cursor.close()
        return success

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return False

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

def actualizar_antecedentes_familiares(diabetes, hta, oncologicos, couagulopatias, alta_genetica, vih_sida,
                                      tuberculosis, alergia, cardiopatias, obesidad, artritis, hemofilia,
                                      mentales, toxicomanias, alcoholismo, hiperlipidemias, otro, id_historial_clinico):
    try:
        cursor = connection.cursor()

        # Llamada al procedimiento almacenado
        sql = """CALL ActualizarAntecedentesFamiliares(
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
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
            print("Actualización exitosa")
        else:
            print("Error al actualizar antecedentes familiares")

        cursor.close()
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
    
def actualizar_antecedentes_no_patologicos(alimentacion, cantidad_alimentacion, fecuencia_alimentacion, habitos_higiene,
                                           alcoholismo, frecuencia_alcoholismo, tabaquismo, numero_cigarros, drogas,
                                           tipo_drogas, inmunizaciones, tipo_inmunizaciones, id_historial_clinico):
    try:
        cursor = connection.cursor()

        # SQL call to the stored procedure
        sql = """CALL ActualizarAntecedentesNoPatologicos(
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, @success)"""
        
        # Parameters for the procedure
        val = (alimentacion, cantidad_alimentacion, fecuencia_alimentacion, habitos_higiene,
               alcoholismo, frecuencia_alcoholismo, tabaquismo, numero_cigarros, drogas,
               tipo_drogas, inmunizaciones, tipo_inmunizaciones, id_historial_clinico)

        # Execute the procedure
        cursor.execute(sql, val)

        # Get the output parameter @success
        cursor.execute("SELECT @success")
        result = cursor.fetchone()
        success = result[0]

        if success:
            print("Actualización exitosa en Antecedentes_no_patologicos")
        else:
            print("Error al actualizar antecedentes no patológicos")

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
    #28
def actualizar_antecedentes_personales_patologicos(
    alergia, reumatismo, diabetes, hipertensivo, its, vih_sida, neurologico, infeccion, 
    parasito_intestinal, quirurgico, hemotransfusion, cardiopatias, enf_renal, cancer, 
    anemia, hemorragias, hepatitis, neumopatias, paludismo, fibre_tifoidea, brucelosis, 
    crisis_convulsivas, enf_mental, traumatico, ulcera, medicamento_actual, otras_patologias, 
    id_historial_clinico):
    try:
        cursor = connection.cursor()

        # Llamada al procedimiento almacenado
        sql = """CALL ActualizarAntecedentesPersonalesPatologicos(
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, @success)"""
        
        # Parámetros para la ejecución del procedimiento
        val = (alergia, reumatismo, diabetes, hipertensivo, its, vih_sida, neurologico, infeccion, 
               parasito_intestinal, quirurgico, hemotransfusion, cardiopatias, enf_renal, cancer, 
               anemia, hemorragias, hepatitis, neumopatias, paludismo, fibre_tifoidea, brucelosis, 
               crisis_convulsivas, enf_mental, traumatico, ulcera, medicamento_actual, otras_patologias, 
               id_historial_clinico)

        # Ejecutar el procedimiento
        cursor.execute(sql, val)

        # Obtener el valor del parámetro de salida @success
        cursor.execute("SELECT @success")
        result = cursor.fetchone()
        success = result[0]

        if success:
            print("Actualización exitosa")
        else:
            print("Error al actualizar antecedentes personales patológicos")

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
    
def actualizar_antecedentes_gineco_obstetricos(
    menarca, ritmo, ivsa, cs, mp_f, gesta, para, cesarea, aborto, fum, doc, docma, 
    antecedentes_peritenales, id_historial_clinico):
    try:
        cursor = connection.cursor()

        # Llamada al procedimiento almacenado
        sql = """CALL ActualizarAntecedentesGinecoObstetricos(
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, @success)"""
        
        # Parámetros para la ejecución del procedimiento
        val = (menarca, ritmo, ivsa, cs, mp_f, gesta, para, cesarea, aborto, fum, 
               doc, docma, antecedentes_peritenales, id_historial_clinico)

        # Ejecutar el procedimiento
        cursor.execute(sql, val)

        # Obtener el valor del parámetro de salida @success
        cursor.execute("SELECT @success")
        result = cursor.fetchone()
        success = result[0]

        if success:
            print("Actualización exitosa")
        else:
            print("Error al actualizar antecedentes gineco-obstétricos")

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
    
def actualizar_interrogatorio_aparato_sistema(
    sintomas_generales, respiratorio, digestivo, nervioso, musculoesqueletico, 
    cardiovascular, genitourinario, endocrino, psiquico, piel_mucosa, 
    organos_sentidos, hematologico_linfatico, cabeza_cuello, organos_reproductivos, 
    id_historial_clinico):
    try:
        cursor = connection.cursor()

        # Llamada al procedimiento almacenado
        sql = """CALL ActualizarInterrogatorioAparatoSistema(
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, @success)"""
        
        # Parámetros para la ejecución del procedimiento
        val = (sintomas_generales, respiratorio, digestivo, nervioso, musculoesqueletico, 
               cardiovascular, genitourinario, endocrino, psiquico, piel_mucosa, 
               organos_sentidos, hematologico_linfatico, cabeza_cuello, organos_reproductivos, 
               id_historial_clinico)

        # Ejecutar el procedimiento
        cursor.execute(sql, val)

        # Obtener el valor del parámetro de salida @success
        cursor.execute("SELECT @success")
        result = cursor.fetchone()
        success = result[0]

        if success:
            print("Actualización exitosa")
        else:
            print("Error al actualizar interrogatorio aparato-sistema")

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
    
def actualizar_exploracion_fisica(
    pulso, temperatura, tension_arterial, frecuencia_cardiaca, frecuencia_respiratoria,
    cabeza, cuello, torax, abdomen, miembros, genitales, id_historial_clinico):
    try:
        cursor = connection.cursor()

        # Llamada al procedimiento almacenado
        sql = """CALL ActualizarExploracionFisica(
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, @success)"""
        
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
            print("Actualización exitosa")
        else:
            print("Error al actualizar exploración física")

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
    
@app.route('/editar_historial_medico/<id>', methods=['POST'])
def editar_historial_medico(id):
    
    id_historial = int(id)
    edad = 49
    motivo_consulta = "Dolor de cabeza persistente"
    padecimiento_actual = "Migraña diagnosticada"
    resultado_laboratorio = "Hemograma normal"
    diagnosticos = "Migraña"
    tratamiento = "Analgesia y descanso"
    fecha = "2024-10-01 10:00:00"
    interrogatorio = True
    curp_persona = "ABC123456789"
    cedula_medico = "MED123456"
    success = False
    success = actualizar_historial_clinico(id_historial, edad, motivo_consulta, padecimiento_actual, 
                                        resultado_laboratorio, diagnosticos, tratamiento, 
                                        fecha, interrogatorio, curp_persona, cedula_medico)

    if success:
        print("La actualización fue exitosa de historial.")
    else:
        print("Hubo un problema con la actualización de historial.")
    
    
    return jsonify({
        'Estado' : success,
        'ID' : id
    })

@app.route('/editar_antecedentes_familiares/<id>', methods=['POST'])
def editar_antecedente_familiar(id):
    
    id_historial = int(id)
    diabetes = "No"
    hta = "Sí"
    oncologicos = "No"
    couagulopatias = "No"
    alta_genetica = "Sí"
    vih_sida = False
    tuberculosis = "No"
    alergia = "Polen"
    cardiopatias = "Sí"
    obesidad = "No"
    artritis = "Sí"
    hemofilia = "No"
    mentales = "No"
    toxicomanias = "No"
    alcoholismo = "Ocasional"
    hiperlipidemias = "No"
    otro = "Sin observaciones"

    # Llamada de ejemplo para actualizar antecedentes familiares
    success = actualizar_antecedentes_familiares(diabetes, hta, oncologicos, couagulopatias, 
                                                alta_genetica, vih_sida, tuberculosis, alergia, cardiopatias, 
                                                obesidad, artritis, hemofilia, mentales, toxicomanias, 
                                                alcoholismo, hiperlipidemias, otro, id_historial)

    if success:
        print("La actualización fue exitosa.")
    else:
        print("Hubo un problema con la actualización.")
    
    
    return jsonify({
        'Estado' : success,
        'ID' : id
    })
    
@app.route('/editar_antecedentes_no_patologicos/<id>', methods=['POST'])
def editar_antecedente_no_patologico(id):
    # Convert the id from the URL to an integer
    id_historial = int(id)
    
    # Sample data for updating the record (could be replaced by data from a POST request)
    alimentacion = "Equilibradaa"
    cantidad_alimentacion = "Moderada"
    fecuencia_alimentacion = 3
    habitos_higiene = "Buenos"
    alcoholismo = "Social"
    frecuencia_alcoholismo = "Mensual"
    tabaquismo = "No"
    numero_cigarros = "0"
    drogas = "No"
    tipo_drogas = ""
    inmunizaciones = True
    tipo_inmunizaciones = "Vacuna A, Vacuna B"
    
    # Call the method to update the record in the database
    success = actualizar_antecedentes_no_patologicos(
        alimentacion, cantidad_alimentacion, fecuencia_alimentacion, habitos_higiene,
        alcoholismo, frecuencia_alcoholismo, tabaquismo, numero_cigarros, drogas,
        tipo_drogas, inmunizaciones, tipo_inmunizaciones, id_historial
    )

    # Return JSON response indicating success or failure
    return jsonify({
        'Estado': success,
        'ID': id
    })

@app.route('/editar_antecedentes_personales_patologicos/<id>', methods=['POST'])
def editar_antecedente_personal_patologico(id):
    id_historial = int(id)
    
    # Datos de ejemplo, estos deberían venir del cuerpo de la solicitud (request) en una aplicación real.
    alergia = "Abejas"
    reumatismo = "No"
    diabetes = "Sí"
    hipertensivo = "No"
    its = "No"
    vih_sida = "No"
    neurologico = "No"
    infeccion = "Sí"
    parasito_intestinal = "No"
    quirurgico = "Sí"
    hemotransfusion = "No"
    cardiopatias = "Sí"
    enf_renal = "No"
    cancer = "No"
    anemia = "Sí"
    hemorragias = "No"
    hepatitis = "No"
    neumopatias = "No"
    paludismo = "No"
    fibre_tifoidea = "No"
    brucelosis = "No"
    crisis_convulsivas = "No"
    enf_mental = "No"
    traumatico = "Sí"
    ulcera = "No"
    medicamento_actual = "Paracetamol"
    otras_patologias = "Ninguna"

    # Llamada de ejemplo para actualizar antecedentes personales patológicos
    success = actualizar_antecedentes_personales_patologicos(
        alergia, reumatismo, diabetes, hipertensivo, its, vih_sida, neurologico, infeccion, 
        parasito_intestinal, quirurgico, hemotransfusion, cardiopatias, enf_renal, cancer, 
        anemia, hemorragias, hepatitis, neumopatias, paludismo, fibre_tifoidea, brucelosis, 
        crisis_convulsivas, enf_mental, traumatico, ulcera, medicamento_actual, otras_patologias, 
        id_historial)

    if success:
        print("La actualización fue exitosa.")
    else:
        print("Hubo un problema con la actualización.")
    
    return jsonify({
        'Estado': success,
        'ID': id
    })

@app.route('/editar_antecedentes_gineco_obstetricos/<id>', methods=['POST'])
def editar_antecedente_gineco_obstetrico(id):
    id_historial = int(id)

    # Datos de ejemplo, estos deberían venir del cuerpo de la solicitud (request) en una aplicación real.
    menarca = "Menarca a los 11 años"
    ritmo = "Regular"
    ivsa = "No"
    cs = "1"
    mp_f = "Ninguna"
    gesta = "2"
    para = "1"
    cesarea = "No"
    aborto = "Sí"
    fum = "2024-06-15"
    doc = "2024-01-20"
    docma = "2023-12-05"
    antecedentes_peritenales = "Sin antecedentes"

    # Llamada de ejemplo para actualizar antecedentes gineco-obstétricos
    success = actualizar_antecedentes_gineco_obstetricos(
        menarca, ritmo, ivsa, cs, mp_f, gesta, para, cesarea, aborto, fum, doc, 
        docma, antecedentes_peritenales, id_historial)

    if success:
        print("La actualización fue exitosa.")
    else:
        print("Hubo un problema con la actualización.")
    
    return jsonify({
        'Estado': success,
        'ID': id
    })

@app.route('/editar_interrogatorio_aparato_sistema/<id>', methods=['POST'])
def editar_interrogatorio_aparato_sistema(id):
    id_historial = int(id)

    # Datos de ejemplo, estos deberían venir del cuerpo de la solicitud (request) en una aplicación real.
    sintomas_generales = "Son síntomas generales"
    respiratorio = "Normal"
    digestivo = "Normal"
    nervioso = "Sin alteraciones"
    musculoesqueletico = "Sin alteraciones"
    cardiovascular = "Sin alteraciones"
    genitourinario = "Normal"
    endocrino = "Normal"
    psiquico = "Estable"
    piel_mucosa = "Normal"
    organos_sentidos = "Sin alteraciones"
    hematologico_linfatico = "Sin alteraciones"
    cabeza_cuello = "Sin alteraciones"
    organos_reproductivos = "Normal"

    # Llamada de ejemplo para actualizar interrogatorio aparato-sistema
    success = actualizar_interrogatorio_aparato_sistema(
        sintomas_generales, respiratorio, digestivo, nervioso, musculoesqueletico, 
        cardiovascular, genitourinario, endocrino, psiquico, piel_mucosa, 
        organos_sentidos, hematologico_linfatico, cabeza_cuello, organos_reproductivos, 
        id_historial)

    if success:
        print("La actualización fue exitosa.")
    else:
        print("Hubo un problema con la actualización.")
    
    return jsonify({
        'Estado': success,
        'ID': id
    })
    
@app.route('/editar_exploracion_fisica/<id>', methods=['POST'])
def editar_exploracion_fisica(id):
    id_historial = int(id)

    # Datos de ejemplo, estos deberían venir del cuerpo de la solicitud (request) en una aplicación real.
    pulso = 72.5
    temperatura = 36.7
    tension_arterial = 120.0
    frecuencia_cardiaca = 75.0
    frecuencia_respiratoria = 18.0
    cabeza = "Normal"
    cuello = "Normal"
    torax = "Normal"
    abdomen = "Normal"
    miembros = "Normal"
    genitales = "Normal"

    # Llamada de ejemplo para actualizar exploración física
    success = actualizar_exploracion_fisica(
        pulso, temperatura, tension_arterial, frecuencia_cardiaca, frecuencia_respiratoria,
        cabeza, cuello, torax, abdomen, miembros, genitales, id_historial)

    if success:
        print("La actualización fue exitosa.")
    else:
        print("Hubo un problema con la actualización.")
    
    return jsonify({
        'Estado': success,
        'ID': id
    })
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)