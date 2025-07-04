-- SQLite
SELECT id,product_name 
    FROM products;


SELECT id,product_name,product_price
    FROM products
    WHERE product_price>50000;


SELECT  product_id,product_name,quantity_purchased
    FROM shopping_carts_products,products
    WHERE products.id=shopping_carts_products.product_id and products.id=1;


SELECT  product_id, SUM(quantity_purchased*product_price) AS total
    FROM shopping_carts_products,products
    WHERE product_id=products.id
    GROUP BY product_id;


SELECT id , user_email, purchase_date
    FROM invoices
    WHERE user_email='miguelsarojas@gmail.com';


SELECT id,total_paid
    FROM invoices
    ORDER BY total_paid DESC;


SELECT ROW_NUMBER() OVER (ORDER BY user_email) AS totalinvoice_id ,user_email,SUM(total_paid) AS invoice_total_amount
    FROM invoices
    GROUP BY user_email;

