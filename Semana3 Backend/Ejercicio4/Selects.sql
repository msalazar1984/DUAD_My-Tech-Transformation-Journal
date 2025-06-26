-- SQLite
SELECT id,nombre_producto 
    FROM productos;


SELECT id,nombre_producto,precio
    FROM productos
    WHERE precio>50000;


SELECT  product_id, COUNT(*) AS total_compras
    FROM shopping_carts_products
    GROUP BY product_id;


SELECT  product_id, SUM(cantidad_comprada*precio) AS monto_total_compras
    FROM shopping_carts_products,productos
    WHERE product_id=productos.id
    GROUP BY product_id;


SELECT email_comprador , COUNT(*) AS total_facturas
    FROM facturas
    GROUP BY email_comprador;


SELECT id,monto_total
    FROM facturas
    ORDER BY monto_total DESC;


SELECT ROW_NUMBER() OVER (ORDER BY email_comprador) AS facturatotal_id ,email_comprador,SUM(monto_total) AS monto_total_facturado
    FROM facturas
    GROUP BY email_comprador;

