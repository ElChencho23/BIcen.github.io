create database hospital;

use hospital;

CREATE TABLE Medico (
    Cedula varchar(20),
    Nombre TEXT,
    Cedula_especialidad TEXT,
    PRIMARY KEY (Cedula)
);

CREATE TABLE Persona (
    Curp varchar(30),
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
    Id INT auto_increment,
    Edad INT,
    Motivo_consulta TEXT,
    Padecimiento_actual TEXT,
    Resultado_laboratorio TEXT,
    Diagnosticos TEXT,
    Tratamiento TEXT,
    Fecha TIMESTAMP,
    Interrogatorio BOOLEAN,
    Curp_persona varchar(30),
    Cedula_medico varchar(20),
    PRIMARY KEY (Id)
);

CREATE TABLE Antecedentes_Familiares (
    Id INT auto_increment,
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
    Id INT auto_increment,
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
    Id INT auto_increment,
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
    Id INT auto_increment,
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
    Id INT auto_increment,
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
    Id Int auto_increment,
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

ALTER TABLE Historial_clinico DROP FOREIGN KEY fk_historial_medica;
ALTER TABLE Historial_clinico DROP FOREIGN KEY fk_historial_medico;
ALTER TABLE Antecedentes_Familiares DROP FOREIGN KEY fk_antecedentes_familiares_historial;
ALTER TABLE Antecedentes_no_patologicos DROP FOREIGN KEY fk_antecedentes_no_patologicos_historial;
ALTER TABLE Antecedentes_personales_patologicos DROP FOREIGN KEY fk_antecedentes_personales_historial;
ALTER TABLE Antecedentes_gineco_obstetricos DROP FOREIGN KEY fk_antecedentes_gineco_historial;
ALTER TABLE Interrogatorio_aparato_sistema DROP FOREIGN KEY fk_interrogatorio_historial;
ALTER TABLE Exploracion_fisica DROP FOREIGN KEY fk_exploracion_historial;

DELIMITER $$

CREATE PROCEDURE InsertarHistorialClinico (
    IN p_edad INT,
    IN p_motivo_consulta TEXT,
    IN p_padecimiento_actual TEXT,
    IN p_resultado_laboratorio TEXT,
    IN p_diagnosticos TEXT,
    IN p_tratamiento TEXT,
    IN p_fecha TIMESTAMP,
    IN p_interrogatorio BOOLEAN,
    IN p_curp_persona VARCHAR(30),
    IN p_cedula_medico VARCHAR(20),
    OUT p_id INT
)
BEGIN
    INSERT INTO Historial_clinico (
        Edad,
        Motivo_consulta,
        Padecimiento_actual,
        Resultado_laboratorio,
        Diagnosticos,
        Tratamiento,
        Fecha,
        Interrogatorio,
        Curp_persona,
        Cedula_medico
    ) 
    VALUES (
        p_edad,
        p_motivo_consulta,
        p_padecimiento_actual,
        p_resultado_laboratorio,
        p_diagnosticos,
        p_tratamiento,
        p_fecha,
        p_interrogatorio,
        p_curp_persona,
        p_cedula_medico
    );
    
    SET p_id = LAST_INSERT_ID();
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE InsertarAntecedentesFamiliares(
    IN p_diabetes VARCHAR(150),
    IN p_hta VARCHAR(150),
    IN p_oncologicos VARCHAR(150),
    IN p_couagulopatias VARCHAR(150),
    IN p_alta_genetica VARCHAR(150),
    IN p_vih_sida BOOLEAN,
    IN p_tuberculosis VARCHAR(150),
    IN p_alergia VARCHAR(150),
    IN p_cardiopatias VARCHAR(150),
    IN p_obesidad VARCHAR(150),
    IN p_artritis VARCHAR(150),
    IN p_hemofilia VARCHAR(150),
    IN p_mentales VARCHAR(150),
    IN p_toxicomanias VARCHAR(150),
    IN p_alcoholismo VARCHAR(150),
    IN p_hiperlipidemias VARCHAR(150),
    IN p_otro TEXT,
    IN p_id_historial_clinico INT,
    OUT p_success BOOLEAN
)
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
        SET p_success = FALSE;

    INSERT INTO Antecedentes_Familiares (
        Diabetes, HTA, Oncologicos, Couagulopatias, Alta_genetica, Vih_sida,
        Tuberculosis, Alergia, Cardiopatias, Obesidad, Artritis, Hemofilia,
        Mentales, Toxicomanias, Alcoholismo, Hiperlipidemias, Otro, Id_historial_clinico
    ) 
    VALUES (
        p_diabetes, p_hta, p_oncologicos, p_couagulopatias, p_alta_genetica, p_vih_sida,
        p_tuberculosis, p_alergia, p_cardiopatias, p_obesidad, p_artritis, p_hemofilia,
        p_mentales, p_toxicomanias, p_alcoholismo, p_hiperlipidemias, p_otro, p_id_historial_clinico
    );

    SET p_success = TRUE;

END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE InsertarAntecedentesNoPatologicos (
    IN p_alimentacion VARCHAR(150),
    IN p_cantidad_alimentacion VARCHAR(150),
    IN p_fecuencia_alimentacion INT,
    IN p_habitos_higiene VARCHAR(150),
    IN p_alcoholismo VARCHAR(150),
    IN p_frecuencia_alcoholismo VARCHAR(150),
    IN p_tabaquismo VARCHAR(150),
    IN p_numero_cigarros VARCHAR(150),
    IN p_drogas VARCHAR(150),
    IN p_tipo_drogas VARCHAR(150),
    IN p_inmunizaciones BOOLEAN,
    IN p_tipo_inmunizaciones VARCHAR(150),
    IN p_id_historial_clinico INT,
    OUT p_success BOOLEAN
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET p_success = FALSE;
        ROLLBACK;
    END;

    START TRANSACTION;

    INSERT INTO Antecedentes_no_patologicos (
        Alimentacion,
        Cantidad_alimentacion,
        Fecuencia_alimentacion,
        Habitos_higiene,
        Alcoholismo,
        Frecuencia_alcoholismo,
        Tabaquismo,
        Numero_cigarros,
        Drogas,
        Tipo_drogas,
        Inmunizaciones,
        Tipo_inmunizaciones,
        Id_historial_clinico
    ) 
    VALUES (
        p_alimentacion,
        p_cantidad_alimentacion,
        p_fecuencia_alimentacion,
        p_habitos_higiene,
        p_alcoholismo,
        p_frecuencia_alcoholismo,
        p_tabaquismo,
        p_numero_cigarros,
        p_drogas,
        p_tipo_drogas,
        p_inmunizaciones,
        p_tipo_inmunizaciones,
        p_id_historial_clinico
    );

    COMMIT;

    SET p_success = TRUE;
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE InsertarAntecedentesPersonalesPatologicos (
    IN p_alergia VARCHAR(150),
    IN p_reumatismo VARCHAR(150),
    IN p_diabetes VARCHAR(150),
    IN p_hipertensivo VARCHAR(150),
    IN p_its VARCHAR(150),
    IN p_vih_sida VARCHAR(150),
    IN p_neurologico VARCHAR(150),
    IN p_infeccion VARCHAR(150),
    IN p_parasito_intestinal TEXT,
    IN p_quirurgico TEXT,
    IN p_hemotransfusion TEXT,
    IN p_cardiopatias TEXT,
    IN p_enf_renal TEXT,
    IN p_cancer TEXT,
    IN p_anemia TEXT,
    IN p_hemorragias TEXT,
    IN p_hepatitis TEXT,
    IN p_neumopatias TEXT,
    IN p_paludismo TEXT,
    IN p_fibre_tifoidea TEXT,
    IN p_brucelosis TEXT,
    IN p_crisis_convulsivas TEXT,
    IN p_enf_mental TEXT,
    IN p_traumatico TEXT,
    IN p_ulcera TEXT,
    IN p_medicamento_actual TEXT,
    IN p_otras_patologias TEXT,
    IN p_id_historial_clinico INT,
    OUT p_success BOOLEAN
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET p_success = FALSE;
        ROLLBACK;
    END;

    START TRANSACTION;

    INSERT INTO Antecedentes_personales_patologicos (
        Alergia,
        Reumatismo,
        Diabetes,
        Hipertensivo,
        ITS,
        Vih_sida,
        Neurologico,
        Infeccion,
        Parasito_intestinal,
        Quirurgico,
        Hemotransfusion,
        Cardiopatias,
        Enf_renal,
        Cancer,
        Anemia,
        Hemorragias,
        Hepatitis,
        Neumopatias,
        Paludismo,
        Fibre_tifoidea,
        Brucelosis,
        Crisis_convulsivas,
        Enf_mental,
        Traumatico,
        Ulcera,
        Medicamento_actual,
        Otras_patologias,
        Id_historial_clinico
    ) 
    VALUES (
        p_alergia,
        p_reumatismo,
        p_diabetes,
        p_hipertensivo,
        p_its,
        p_vih_sida,
        p_neurologico,
        p_infeccion,
        p_parasito_intestinal,
        p_quirurgico,
        p_hemotransfusion,
        p_cardiopatias,
        p_enf_renal,
        p_cancer,
        p_anemia,
        p_hemorragias,
        p_hepatitis,
        p_neumopatias,
        p_paludismo,
        p_fibre_tifoidea,
        p_brucelosis,
        p_crisis_convulsivas,
        p_enf_mental,
        p_traumatico,
        p_ulcera,
        p_medicamento_actual,
        p_otras_patologias,
        p_id_historial_clinico
    );

    COMMIT;

    SET p_success = TRUE;
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE InsertarAntecedentesGinecoObstetricos (
    IN p_menarca VARCHAR(150),
    IN p_ritmo VARCHAR(150),
    IN p_ivsa VARCHAR(150),
    IN p_cs VARCHAR(150),
    IN p_mp_f VARCHAR(150),
    IN p_gesta VARCHAR(150),
    IN p_para VARCHAR(150),
    IN p_cesarea VARCHAR(150),
    IN p_aborto VARCHAR(150),
    IN p_fum VARCHAR(150),
    IN p_doc VARCHAR(150),
    IN p_docma VARCHAR(150),
    IN p_antecedentes_peritenales VARCHAR(150),
    IN p_id_historial_clinico INT,
    OUT p_success BOOLEAN
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET p_success = FALSE;
        ROLLBACK;
    END;

    START TRANSACTION;

    INSERT INTO Antecedentes_gineco_obstetricos (
        Menarca,
        Ritmo,
        Ivsa,
        Cs,
        Mp_f,
        Gesta,
        Para,
        Cesarea,
        Aborto,
        FUM,
        DOC,
        DOCMA,
        Antecedentes_peritenales,
        Id_historial_medico
    ) 
    VALUES (
        p_menarca,
        p_ritmo,
        p_ivsa,
        p_cs,
        p_mp_f,
        p_gesta,
        p_para,
        p_cesarea,
        p_aborto,
        p_fum,
        p_doc,
        p_docma,
        p_antecedentes_peritenales,
        p_id_historial_clinico
    );

    COMMIT;

    SET p_success = TRUE;
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE InsertarInterrogatorioAparatoSistema (
    IN p_sistomas_generales TEXT,
    IN p_respiratorio TEXT,
    IN p_digestivo TEXT,
    IN p_nervioso TEXT,
    IN p_musculoesqueletico TEXT,
    IN p_cardiovascular TEXT,
    IN p_genitourinario TEXT,
    IN p_endoctrico TEXT,
    IN p_psiquico TEXT,
    IN p_piel_mucosa TEXT,
    IN p_organos_sentidos TEXT,
    IN p_hematico_linfatico TEXT,
    IN p_cabeza_cuello TEXT,
    IN p_organos_reproductivos TEXT,
    IN p_id_historial_clinico INT,
    OUT p_success BOOLEAN
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET p_success = FALSE;
        ROLLBACK;
    END;

    START TRANSACTION;

    INSERT INTO Interrogatorio_aparato_sistema (
        Sistomas_generales,
        Respiratorio,
        Digestivo,
        Nervioso,
        Musculoesqueletico,
        Cardiovascular,
        Genitourinario,
        Endoctrico,
        Psiquico,
        Piel_mucosa,
        Organos_sentidos,
        Hematico_linfatico,
        Cabeza_cuello,
        Organos_reproductivos,
        Id_historial_clinico
    ) 
    VALUES (
        p_sistomas_generales,
        p_respiratorio,
        p_digestivo,
        p_nervioso,
        p_musculoesqueletico,
        p_cardiovascular,
        p_genitourinario,
        p_endoctrico,
        p_psiquico,
        p_piel_mucosa,
        p_organos_sentidos,
        p_hematico_linfatico,
        p_cabeza_cuello,
        p_organos_reproductivos,
        p_id_historial_clinico
    );

    COMMIT;

    SET p_success = TRUE;
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE InsertarExploracionFisica (
    IN p_pulso FLOAT,
    IN p_temperatura FLOAT,
    IN p_tension_arterial FLOAT,
    IN p_frecuencia_cardiaca FLOAT,
    IN p_frecuencia_respiratoria FLOAT,
    IN p_cabeza TEXT,
    IN p_cuello TEXT,
    IN p_torax TEXT,
    IN p_abdomen TEXT,
    IN p_miembros TEXT,
    IN p_genitales TEXT,
    IN p_id_historial_clinico INT,
    OUT p_success BOOLEAN
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SET p_success = FALSE;
        ROLLBACK;
    END;

    START TRANSACTION;

    INSERT INTO Exploracion_fisica (
        Pulso,
        Temperatura,
        Tension_arterial,
        Frecuencia_cardiaca,
        Frecuencia_respiratoria,
        Cabeza,
        Cuello,
        Torax,
        Abdomen,
        Miembros,
        Genitales,
        Id_historial_clinico
    ) 
    VALUES (
        p_pulso,
        p_temperatura,
        p_tension_arterial,
        p_frecuencia_cardiaca,
        p_frecuencia_respiratoria,
        p_cabeza,
        p_cuello,
        p_torax,
        p_abdomen,
        p_miembros,
        p_genitales,
        p_id_historial_clinico
    );

    COMMIT;

    SET p_success = TRUE;
END$$

DELIMITER ;
