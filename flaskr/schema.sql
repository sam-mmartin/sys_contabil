DROP TABLE IF EXISTS register;
DROP TABLE IF EXISTS operation;
DROP TABLE IF EXISTS category;

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

