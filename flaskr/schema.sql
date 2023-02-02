DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS register;
DROP TABLE IF EXISTS operation;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS sum_credit_anual;

CREATE TABLE user (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   username TEXT UNIQUE NOT NULL,
   password TEXT NOT NULL
);

CREATE TABLE operation (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   description TEXT NOT NULL,
   date_create DATE NOT NULL,
   date_update DATE NOT NULL
);

CREATE TABLE category (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   description TEXT NOT NULL,
   date_create DATE NOT NULL,
   date_update DATE NOT NULL
);

CREATE TABLE register (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   description TEXT NOT NULL,
   amount REAL NOT NULL,
   operation_id INTEGER NOT NULL,
   category_id INTEGER NOT NULL,
   date_register DATE NOT NULL,
   date_update DATE NOT NULL,
   user_id INTEGER NOT NULL,
   FOREIGN KEY (operation_id) REFERENCES operation (id),
   FOREIGN KEY (category_id) REFERENCES category (id),
   FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE sum_credit_anual (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   credit_amount REAL NOT NULL,
   credit_month INTEGER NOT NULL,
   credit_year, INTEGER NOT NULL,
   date_create DATE NOT NULL,
   date_update DATE NOT NULL,
   user_id INTEGER NOT NULL,
   FOREIGN KEY (user_id) REFERENCES user (id)
);

INSERT INTO operation (id, description, date_create, date_update) VALUES (1, 'Debito', '2023-02-02', '2023-02-02');
INSERT INTO operation (id, description, date_create, date_update) VALUES (2, 'Credito', '2023-02-02', '2023-02-02');

INSERT INTO category (id, description, date_create, date_update) VALUES (1, 'Fatura', '2023-02-02', '2023-02-02');
INSERT INTO category (id, description, date_create, date_update) VALUES (2, 'Fixo', '2023-02-02', '2023-02-02');
INSERT INTO category (id, description, date_create, date_update) VALUES (3, 'Variavel', '2023-02-02', '2023-02-02');

INSERT INTO register (id, description, amount, operation_id, category_id, date_register, date_update, user_id) 
VALUES (1, 'Carro', 1665.66, 1, 2, '2023-01-20', '2023-02-02', 1);
INSERT INTO register (id, description, amount, operation_id, category_id, date_register, date_update, user_id) 
VALUES (2, 'Salario', 4751.36, 2, 2, '2023-01-20', '2023-02-02', 1);
