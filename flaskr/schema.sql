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

CREATE TABLE sum_anual (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   amount REAL NOT NULL,
   month INTEGER NOT NULL,
   year INTEGER NOT NULL,
   date_create DATE NOT NULL,
   date_update DATE NOT NULL,
   operation_id INTEGER NOT NULL,
   user_id INTEGER,
   FOREIGN KEY (user_id) REFERENCES user (id),
   FOREIGN KEY (operation_id) REFERENCES operation (id)
);

INSERT INTO operation (id, description, date_create, date_update) VALUES (1, 'Debito', '2023-02-02', '2023-02-02');
INSERT INTO operation (id, description, date_create, date_update) VALUES (2, 'Credito', '2023-02-02', '2023-02-02');

INSERT INTO category (id, description, date_create, date_update) VALUES (1, 'Fatura', '2023-02-02', '2023-02-02');
INSERT INTO category (id, description, date_create, date_update) VALUES (2, 'Fixo', '2023-02-02', '2023-02-02');
INSERT INTO category (id, description, date_create, date_update) VALUES (3, 'Variavel', '2023-02-02', '2023-02-02');

INSERT INTO register (id, description, amount, operation_id, category_id, date_register, date_update, user_id) 
VALUES (1, 'Carro', 1665.66, 1, 2, '2023-01-20', '2023-02-02', 1);
INSERT INTO register (id, description, amount, operation_id, category_id, date_register, date_update, user_id) 
VALUES (2, 'Emprestimo', 624.38, 1, 2, '2023-01-20', '2023-02-02', 1);
INSERT INTO register (id, description, amount, operation_id, category_id, date_register, date_update, user_id) 
VALUES (3, 'Fatura ourocard', 317.0, 1, 1, '2023-01-20', '2023-02-02', 1);
INSERT INTO register (id, description, amount, operation_id, category_id, date_register, date_update, user_id) 
VALUES (4, 'Fatura pão de açucar', 276.0, 1, 1, '2023-01-20', '2023-02-02', 1);
INSERT INTO register (id, description, amount, operation_id, category_id, date_register, date_update, user_id) 
VALUES (5, 'Fatura samsung', 245.0, 1, 1, '2023-01-20', '2023-02-02', 1);
INSERT INTO register (id, description, amount, operation_id, category_id, date_register, date_update, user_id) 
VALUES (6, 'Fatura inter', 244.0, 1, 1, '2023-01-20', '2023-02-02', 1);
INSERT INTO register (id, description, amount, operation_id, category_id, date_register, date_update, user_id) 
VALUES (7, 'Cheque especial', 234.66, 1, 3, '2023-01-20', '2023-02-02', 1);
INSERT INTO register (id, description, amount, operation_id, category_id, date_register, date_update, user_id) 
VALUES (8, 'Consorcio eletronico', 140.11, 1, 2, '2023-01-10', '2023-02-02', 1);
INSERT INTO register (id, description, amount, operation_id, category_id, date_register, date_update, user_id) 
VALUES (9, 'Fatura itau', 84.0, 1, 1, '2023-01-20', '2023-02-02', 1);
INSERT INTO register (id, description, amount, operation_id, category_id, date_register, date_update, user_id) 
VALUES (10, 'Consorcio gamer', 72.79, 1, 2, '2023-01-10', '2023-02-02', 1);
INSERT INTO register (id, description, amount, operation_id, category_id, date_register, date_update, user_id) 
VALUES (11, 'Fatura mercado pago', 65.0, 1, 1, '2023-01-20', '2023-02-02', 1);
INSERT INTO register (id, description, amount, operation_id, category_id, date_register, date_update, user_id) 
VALUES (12, 'ourocap', 50.0, 1, 2, '2023-01-24', '2023-02-02', 1);

INSERT INTO register (id, description, amount, operation_id, category_id, date_register, date_update, user_id) 
VALUES (13, 'Salario', 4751.36, 2, 2, '2023-01-20', '2023-02-02', 1);
INSERT INTO register (id, description, amount, operation_id, category_id, date_register, date_update, user_id) 
VALUES (14, 'Markin', 300, 2, 3, '2023-01-09', '2023-02-02', 1);
