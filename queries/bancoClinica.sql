CREATE DATABASE clinica;

CREATE TABLE paciente(
    id SERIAL PRIMARY KEY,
    id_telegram VARCHAR(225),
    F_Name VARCHAR(255),
    L_Name VARCHAR(255),
    UNIQUE (id_telegram)
);

INSERT INTO paciente(id_telegram, F_Name, L_Name ) VALUES ('','','');

CREATE TABLE consultas(
    id SERIAL PRIMARY KEY,
    paciente VARCHAR(255),
    id_telegram VARCHAR (255),
    status VARCHAR(255), 
    date TIMESTAMP        
);

INSERT INTO consultas(status, date) VALUES ('disponivel', '2021-11-01 13:00:00');
INSERT INTO consultas(status, date) VALUES ('disponivel', '2021-11-01 13:30:00');
INSERT INTO consultas(status, date) VALUES ('disponivel', '2021-11-01 14:00:00');
INSERT INTO consultas(status, date) VALUES ('disponivel', '2021-11-01 14:30:00');
INSERT INTO consultas(status, date) VALUES ('disponivel', '2021-11-01 15:00:00');
INSERT INTO consultas(status, date) VALUES ('disponivel', '2021-11-01 15:30:00');
INSERT INTO consultas(status, date) VALUES ('disponivel', '2021-11-01 16:00:00');
INSERT INTO consultas(status, date) VALUES ('disponivel', '2021-11-01 16:30:00');
==============================================================================================|
INSERT INTO consultas(paciente, status, date) VALUES ('' ,'disponivel', '2021-11-02 HH:MM:SS');
INSERT INTO consultas(paciente, status, date) VALUES ('' ,'disponivel', '2021-11-03 HH:MM:SS');
INSERT INTO consultas(paciente, status, date) VALUES ('' ,'disponivel', '2021-11-04 HH:MM:SS');
INSERT INTO consultas(paciente, status, date) VALUES ('' ,'disponivel', '2021-11-04 HH:MM:SS');

\l list databases
\c [DBNAME] connect to new database, e.g., \c template1
\dt list tables of the public schema