CREATE TABLE kmCar(
    id SERIAL PRIMARY KEY,
    brand varchar(255),
    model varchar(255) NOT NULL,
    power varchar(225) NOT NULL,
    year varchar(255) NOT NULL,
    transference varchar(255) NOT NULL,
    km int NOT NULL,
    fuel varchar(255) NOT NULL,
    final_license_plate varchar(255) NOT NULL,
    color varchar(255) NOT NULL,
    licensed varchar(255) NOT NULL,
    IPVApaid varchar(255) NOT NULL,
    price money,
    status varchar(255)
);

INSERT INTO kmCar(brand, model, power, year,transference,km ,fuel, final_license_plate, color, licensed, IPVApaid, price,status) VALUES ('chevrolet','celta', '2.0', '2012','mecanico',100000,'flex', '4', 'prata','sim','sim', 20000.00,'ativo');
INSERT INTO kmCar(brand, model, power, year,transference,km ,fuel, final_license_plate, color, licensed, IPVApaid, price,status) VALUES ('tesla','Model S', '1.034 cv', '2021','automatico', 1000, 'eletrico','7', 'vermelho','sim','sim', 667200.00,'ativo');
INSERT INTO kmCar(brand, model, power, year,transference,km ,fuel, final_license_plate, color, licensed, IPVApaid, price,status) VALUES ('chevrolet','onix', '2.0', '2019','mecanico', 2300, 'flex','5', 'azul','sim','sim', 54200.00,'ativo');
INSERT INTO kmCar(brand, model, power, year,transference,km ,fuel, final_license_plate, color, licensed, IPVApaid, price,status) VALUES ('fiat','toro', '4.0', '2020','automatico', 5020, 'flex','8', 'prata','sim','sim', 92990.00,'ativo');
INSERT INTO kmCar(brand, model, power, year,transference,km ,fuel, final_license_plate, color, licensed, IPVApaid, price,status) VALUES ('toyota','hilux', '4.0', '2019','automatico', 36900, 'disel','1', 'prata','sim','sim', 120000.00,'ativo');
INSERT INTO kmCar(brand, model, power, year,transference,km ,fuel, final_license_plate, color, licensed, IPVApaid, price,status) VALUES ('chevrolet','onix', '1.7', '2018','mecanico', 81000, 'flex','0', 'preto','sim','sim', 41200.00,'ativo');

CREATE TABLE kmMotorcicle(
    id SERIAL PRIMARY KEY,
    brand varchar(255),
    model varchar(255) NOT NULL,
    cc int NOT NULL,         
    year varchar(255) NOT NULL,
    partida varchar(255) NOT NULL,
    marchas int NOT NULL,
    refrigeracao varchar(255) NOT NULL,
    km int NOT NULL,
    alimentação varchar(255) NOT NULL,
    fuel varchar(255) NOT NULL,
    horseP varchar(255),
    final_license_plate varchar(255) NOT NULL,
    color varchar(255),
    licensed varchar(255) NOT NULL,
    IPVApaid varchar(255) NOT NULL,
    price money,
    status varchar(255)
);

INSERT INTO kmMotorcicle(brand, model, cc, year, partida ,marchas ,refrigeracao ,km ,alimentação, fuel, horseP, final_license_plate, color, licensed, IPVApaid, price,status) VALUES ('yamaha','fazer','250','2020','elétrica',5,'ar',0,'injeção eletronica','gasolina','23 cavalos','9','vermelha','sim','sim', 21000.00,'ativo');

\l list databases
\c [DBNAME] connect to new database, e.g., \c template1
\dt list tables of the public schema