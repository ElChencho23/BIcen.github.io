create database hospital;

use hospital;

CREATE TABLE Medico (
    Cedula INT,
    Nombre TEXT,
    Cedula_especialidad TEXT,
    PRIMARY KEY (Cedula)
);

CREATE TABLE Persona (
    Curp INT,
    Nombre VARCHAR(150),
    Fecha_nacimiento DATE,
    Grupo_Sanguineo VARCHAR(150),
    Jurisdiccion VARCHAR(150),
    Escolaridad VARCHAR(150),
    Edad INT,
    Sexo VARCHAR(150),
    Estado_civil VARCHAR(150),
    Ocupacion VARCHAR(150),
    Tipo_seguro VARCHAR(150),
    Calle VARCHAR(150),
    Num INT,
    Colonia VARCHAR(150),
    Municipio VARCHAR(150),
    Lugar_procedencia VARCHAR(150),
    Telefono BIGINT,
    AGEB VARCHAR(150),
    Alergia BOOLEAN,
    Tipo_alergia VARCHAR(150),
    Id_unidad_medica INT,
    PRIMARY KEY (Curp)
);

CREATE TABLE Historial_clinico (
    Id INT,
    Edad INT,
    Motivo_consulta TEXT,
    Padecimiento_actual TEXT,
    Resultado_laboratorio TEXT,
    Diagnosticos TEXT,
    Tratamiento TEXT,
    Fecha TIMESTAMP,
    Interrogatorio BOOLEAN,
    Curp_persona INT,
    Cedula_medico INT,
    PRIMARY KEY (Id)
);

CREATE TABLE Antecedentes_Familiares (
    Id INT,
    Diabetes VARCHAR(150),
    HTA VARCHAR(150),
    Oncologicos VARCHAR(150),
    Couagulopatias VARCHAR(150),
    Alta_genetica VARCHAR(150),
    Vih_sida BOOLEAN,
    Tuberculosis VARCHAR(150),
    Alergia VARCHAR(150),
    Cardiopatias VARCHAR(150),
    Obesidad VARCHAR(150),
    Artritis VARCHAR(150),
    Hemofilia VARCHAR(150),
    Mentales VARCHAR(150),
    Toxicomanias VARCHAR(150),
    Alcoholismo VARCHAR(150),
    Hiperlipidemias VARCHAR(150),
    Otro TEXT,
    Id_historial_clinico INT,
    PRIMARY KEY (Id)
);

CREATE TABLE Antecedentes_no_patologicos (
    Id INT,
    Alimentacion VARCHAR(150),
    Cantidad_alimentacion VARCHAR(150),
    Fecuencia_alimentacion INT,
    Habitos_higiene VARCHAR(150),
    Alcoholismo VARCHAR(150),
    Frecuencia_alcoholismo VARCHAR(150),
    Tabaquismo VARCHAR(150),
    Numero_cigarros VARCHAR(150),
    Drogas VARCHAR(150),
    Tipo_drogas VARCHAR(150),
    Inmunizaciones BOOLEAN,
    Tipo_inmunizaciones VARCHAR(150),
    Id_historial_clinico INT,
    PRIMARY KEY (Id)
);

CREATE TABLE Antecedentes_personales_patologicos (
    Id INT,
    Alergia VARCHAR(150),
    Reumatismo VARCHAR(150),
    Diabetes VARCHAR(150),
    Hipertensivo VARCHAR(150),
    ITS VARCHAR(150),
    Vih_sida VARCHAR(150),
    Neurologico VARCHAR(150),
    Infeccion VARCHAR(150),
    Parasito_intestinal TEXT,
    Quirurgico TEXT,
    Hemotransfusion TEXT,
    Cardiopatias TEXT,
    Enf_renal TEXT,
    Cancer TEXT,
    Anemia TEXT,
    Hemorragias TEXT,
    Hepatitis TEXT,
    Neumopatias TEXT,
    Paludismo TEXT,
    Fibre_tifoidea TEXT,
    Brucelosis TEXT,
    Crisis_convulsivas TEXT,
    Enf_mental TEXT,
    Traumatico TEXT,
    Ulcera TEXT,
    Medicamento_actual TEXT,
    Otras_patologias TEXT,
    Id_historial_clinico INT,
    PRIMARY KEY (Id)
);

CREATE TABLE Antecedentes_gineco_obstetricos (
    Id INT,
    Menarca VARCHAR(150),
    Ritmo VARCHAR(150),
    Ivsa VARCHAR(150),
    Cs VARCHAR(150),
    Mp_f VARCHAR(150),
    Gesta VARCHAR(150),
    Para VARCHAR(150),
    Cesarea VARCHAR(150),
    Aborto VARCHAR(150),
    FUM VARCHAR(150),
    DOC VARCHAR(150),
    DOCMA VARCHAR(150),
    Antecedentes_peritenales VARCHAR(150),
    Id_historial_medico INT,
    PRIMARY KEY (Id)
);

CREATE TABLE Interrogatorio_aparato_sistema (
    Id INT,
    Sistomas_generales TEXT,
    Respiratorio TEXT,
    Digestivo TEXT,
    Nervioso TEXT,
    Musculoesqueletico TEXT,
    Cardiovascular TEXT,
    Genitourinario TEXT,
    Endoctrico TEXT,
    Psiquico TEXT,
    Piel_mucosa TEXT,
    Organos_sentidos TEXT,
    Hematico_linfatico TEXT,
    Cabeza_cuello TEXT,
    Organos_reproductivos TEXT,
    Id_historial_clinico INT,
    PRIMARY KEY (Id)
);

CREATE TABLE Exploracion_fisica (
    Id INT,
    Pulso FLOAT,
    Temperatura FLOAT,
    Tension_arterial FLOAT,
    Frecuencia_cardiaca FLOAT,
    Frecuencia_respiratoria FLOAT,
    Cabeza TEXT,
    Cuello TEXT,
    Torax TEXT,
    Abdomen TEXT,
    Miembros TEXT,
    Genitales TEXT,
    Id_historial_clinico INT,
    PRIMARY KEY (Id)
);
    
ALTER TABLE Historial_clinico
ADD CONSTRAINT fk_historial_medica
FOREIGN KEY (Curp_persona) REFERENCES Persona(Curp);

ALTER TABLE Historial_clinico
ADD CONSTRAINT fk_historial_medico
FOREIGN KEY (Cedula_medico) REFERENCES Medico(Cedula);

ALTER TABLE Antecedentes_Familiares
ADD CONSTRAINT fk_antecedentes_familiares_historial
FOREIGN KEY (Id_historial_clinico) REFERENCES Historial_clinico(Id);

ALTER TABLE Antecedentes_no_patologicos
ADD CONSTRAINT fk_antecedentes_no_patologicos_historial
FOREIGN KEY (Id_historial_clinico) REFERENCES Historial_clinico(Id);

ALTER TABLE Antecedentes_personales_patologicos
ADD CONSTRAINT fk_antecedentes_personales_historial
FOREIGN KEY (Id_historial_clinico) REFERENCES Historial_clinico(Id);

ALTER TABLE Antecedentes_gineco_obstetricos
ADD CONSTRAINT fk_antecedentes_gineco_historial
FOREIGN KEY (Id_historial_medico) REFERENCES Historial_clinico(Id);

ALTER TABLE Interrogatorio_aparato_sistema
ADD CONSTRAINT fk_interrogatorio_historial
FOREIGN KEY (Id_historial_clinico) REFERENCES Historial_clinico(Id);

ALTER TABLE Exploracion_fisica
ADD CONSTRAINT fk_exploracion_historial
FOREIGN KEY (Id_historial_clinico) REFERENCES Historial_clinico(Id);
