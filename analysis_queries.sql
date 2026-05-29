"C:/Users/HP/Desktop/clothing-brand-analytics/fashion_sales_sql.csv"
CREATE DATABASE clothing_brand_analysis;

USE clothing_brand_analysis;

CREATE TABLE fashion_sales (
    brand VARCHAR(100),
    category VARCHAR(100),
    selling_price INT,
    mrp INT,
    star_rating FLOAT
);

INSERT INTO fashion_sales
(brand, category, selling_price, mrp, star_rating)
VALUES
('ZARA','Jeans',1499,1999,4.5),
('H&M','Tshirt',799,999,4.2),
('BIBA','Kurta',1299,1799,4.4),
('NIKE','Shoes',2999,3999,4.8),
('PUMA','Tracksuit',2499,3499,4.3),
('LEVIS','Jeans',1999,2599,4.6),
('ADIDAS','Shoes',3499,4999,4.7),
('ZARA','Top',1199,1599,4.1),
('H&M','Dress',1599,2199,4.0),
('BIBA','Suit',2299,2999,4.5);

SELECT * FROM fashion_sales;

SELECT brand,
SUM(selling_price) AS total_sales
FROM fashion_sales
GROUP BY brand
ORDER BY total_sales DESC
LIMIT 10;