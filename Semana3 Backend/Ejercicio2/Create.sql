-- SQLite
CREATE TABLE invoices(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number VARCHAR(20),
    purchase_date DATE,
    user_email VARCHAR(254),
    total_paid INT);


CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_code VARCHAR(20),
    product_name TEXT,
    product_price REAL,
    arrival_date DATE,
    product_brand VARCHAR(30));


CREATE TABLE products_invoices(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INT REFERENCES productos(id),
    invoice_id INT REFERENCES facturas(id),
    quantity_purchased INT,
    total_paid REAL);


CREATE TABLE shopping_carts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shopping_cart_code VARCHAR(15),
    purchase_date DATE,
    total_paid REAL,
    user_email VARCHAR(254),
    status VARCHAR(20));


CREATE TABLE shopping_carts_products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shopping_cart_id INT REFERENCES shopping_carts(id),
    product_id INT REFERENCES productos(id),
    quantity_purchased INT);





