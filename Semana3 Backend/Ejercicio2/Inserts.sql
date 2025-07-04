-- SQLite
INSERT INTO products (product_code, product_name, product_price, arrival_date,product_brand)
    VALUES ('CMP001-001','Mouse',25000,'24/09/2024','Microsoft');


INSERT INTO products (product_code, product_name, product_price, arrival_date,product_brand)
    VALUES ('CMP002-002','Audifonos',45000,'12/09/2024','Oticon');


INSERT INTO products (product_code, product_name, product_price, arrival_date,product_brand)
    VALUES ('CMP003-003','Pantalla Led',250000,'02/04/2024','Sansumg');


INSERT INTO products (product_code, product_name, product_price, arrival_date,product_brand)
    VALUES ('CMP004-004','Tarjeta Madre',125000,'03/04/2024','AMD');


INSERT INTO products (product_code, product_name, product_price, arrival_date,product_brand)
    VALUES ('CMP005-005','Laptop',250000,'01/06/2025','Lenovo');


INSERT INTO products (product_code, product_name, product_price, arrival_date,product_brand)
    VALUES ('CMP006-006','RAM',120000,'15/05/2025','Kingston');



INSERT INTO invoices (invoice_number, purchase_date, user_email, total_paid)
    VALUES ('FACT-001-2025','05/01/2025','miguelsarojas@gmail.com',25000);


INSERT INTO invoices (invoice_number, purchase_date, user_email, total_paid)
    VALUES ('FACT-002-2025','06/01/2025','mariauxrojas@gmail.com',95000);


INSERT INTO invoices (invoice_number, purchase_date, user_email, total_paid)
    VALUES ('FACT-003-2025','05/04/2025','carolyns@gmail.com',115000);


INSERT INTO invoices (invoice_number, purchase_date, user_email, total_paid)
    VALUES ('FACT-004-2025','02/02/2025','manuel.ortiz@outlook.com',25000);


INSERT INTO invoices (invoice_number, purchase_date, user_email, total_paid)
    VALUES ('FACT-005-2025','01/03/2025','mario.quiros1984@gmail.com',250000);


INSERT INTO products_invoices (product_id, invoice_id, quantity_purchased, total_paid)
    VALUES (1,1,1,25000);


INSERT INTO products_invoices (product_id, invoice_id, quantity_purchased, total_paid)
    VALUES (2,1,2,50000);


INSERT INTO products_invoices (product_id, invoice_id, quantity_purchased, total_paid)
    VALUES (2,2,1,45000);


INSERT INTO products_invoices (product_id, invoice_id, quantity_purchased, total_paid)
    VALUES (3,2,2,90000);


INSERT INTO products_invoices (product_id, invoice_id, quantity_purchased, total_paid)
    VALUES (3,1,1,25000);


INSERT INTO products_invoices (product_id, invoice_id, quantity_purchased, total_paid)
    VALUES (4,1,1,25000);


INSERT INTO products_invoices (product_id, invoice_id, quantity_purchased, total_paid)
    VALUES (5,4,2,250000);


INSERT INTO shopping_carts (shopping_cart_code, purchase_date, total_paid, user_email,status)
    VALUES ('SC-001','05/01/2025',340000,'miguelsarojas@gmail.com','Enviado');


INSERT INTO shopping_carts (shopping_cart_code, purchase_date, total_paid, user_email,status)
    VALUES ('SC-002','02/02/2025',120000,'mariauxrojas@gmail.com','En Proceso');


INSERT INTO shopping_carts (shopping_cart_code, purchase_date, total_paid, user_email,status)
    VALUES ('SC-003','14/02/2025',120000,'carolyns@gmail.com','Enviado');


INSERT INTO shopping_carts (shopping_cart_code, purchase_date, total_paid, user_email,status)
    VALUES ('SC-004','01/06/2025',250000,'manuel.ortiz@outlook.com','Enviado');


INSERT INTO shopping_carts_products (shopping_cart_id, product_id, quantity_purchased)
    VALUES (1,1,10);


INSERT INTO shopping_carts_products (shopping_cart_id, product_id, quantity_purchased)
    VALUES (1,2,2);


INSERT INTO shopping_carts_products (shopping_cart_id, product_id, quantity_purchased)
    VALUES (2,5,1);


INSERT INTO shopping_carts_products (shopping_cart_id, product_id, quantity_purchased)
    VALUES (3,2,2);


INSERT INTO shopping_carts_products (shopping_cart_id, product_id, quantity_purchased)
    VALUES (3,1,1);


INSERT INTO shopping_carts_products (shopping_cart_id, product_id, quantity_purchased)
    VALUES (4,4,2);

