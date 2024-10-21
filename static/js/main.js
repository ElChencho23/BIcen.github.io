const data = {
    edad: 35,
    motivo_consulta: "Consulta de rutina",
    padecimiento_actual: "Ninguno",
    resultado_laboratorio: "Laboratorio normal",
    diagnosticos: "Sin diagnóstico",
    tratamiento: "Descanso",
    interrogatorio: true,
    curp_persona: "CURP123456ABC",
    cedula_medico: "MED12345"
};

fetch('/Insertar_historial_medico', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
})
    .then(response => response.json())
    .then(data => {
        if (data.Estado) {
            document.getElementById('resultado').textContent = `El historial médico fue insertado con éxito. ID generado: ${data.ID}`;
        } else {
            document.getElementById('resultado').textContent = 'Error al insertar el historial médico.';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('resultado').textContent = 'Error de conexión con la API.';
    });