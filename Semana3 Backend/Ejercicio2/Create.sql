-- SQLite
CREATE TABLE facturas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_factura VARCHAR(20),
    fecha_compra DATE,
    email_comprador VARCHAR(25),
    monto_total INT);


CREATE TABLE productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cod_producto VARCHAR(20),
    nombre_producto TEXT,
    precio REAL,
    fecha_ingreso DATE,
    marca VARCHAR(30));


CREATE TABLE productos_facturas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INT REFERENCES productos(id),
    factura_id INT REFERENCES facturas(id),
    cantidad_comprada INT,
    monto_total REAL);


CREATE TABLE shopping_carts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shopping_cart_code VARCHAR(15),
    fecha_compra DATE,
    monto_total REAL,
    user_email VARCHAR(254),
    estado VARCHAR(20));


CREATE TABLE shopping_carts_products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shopping_cart_id INT REFERENCES shopping_cart(id),
    product_id INT REFERENCES productos(id),
    cantidad_comprada INT);





