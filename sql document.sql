create database document;
use document;
select * from transaction;
#mean (itemgrams)
select avg(itemgrams) as avg_for_itemgrams from transaction;

#median 
SELECT itemgrams AS median_itemgrams
FROM (
    SELECT itemgrams, ROW_NUMBER() OVER (ORDER BY itemgrams) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM transaction
) AS subquery
WHERE row_num = (total_count + 1) / 2 OR row_num = (total_count + 2) / 2;

#mode 
SELECT itemgrams AS mode_for_itemgrams
FROM (
    SELECT itemgrams, COUNT(*) AS frequency
    FROM transaction
    GROUP BY itemgrams
    ORDER BY frequency DESC
    LIMIT 1
) AS subquery;

#standard deviation
SELECT STDDEV(itemgrams) AS stddev_itemgrams
FROM transaction;

#variance
SELECT VARIANCE(itemgrams) AS variance_itemgrams
FROM transaction;

#range
SELECT MAX(itemgrams) - MIN(itemgrams) AS range_load_cells
FROM transaction;

#skewness
SELECT 
    (SUM(POWER(itemgrams - (SELECT AVG(itemgrams) FROM transaction), 3)) / 
    (COUNT(*) * POWER((SELECT STDDEV(itemgrams) FROM transaction), 3))) AS skewness_itemgrams
FROM transaction;

#kurtosis
SELECT 
    ((SUM(POWER(itemgrams - (SELECT AVG(itemgrams) FROM transaction), 4)) / 
    (COUNT(*) * POWER((SELECT STDDEV(itemgrams) FROM transaction), 4))) - 3) AS kurtosis_itemgrams
FROM transaction;

select * from transaction;
#mean (itemnetweight)
select avg(itemnetweight) as avg_itemnetweight from transaction;

#median
select itemnetweight as median_itemnetweight 
from (
 SELECT itemnetweight, ROW_NUMBER() OVER (ORDER BY itemnetweight) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM transaction
) AS subquery
WHERE row_num = (total_count + 1) / 2 OR row_num = (total_count + 2) / 2;

#mode 
SELECT itemnetweight AS mode_for_itemnetweight
FROM (
    SELECT itemnetweight, COUNT(*) AS frequency
    FROM transaction
    GROUP BY itemnetweight
    ORDER BY count(*) DESC
    LIMIT 1
) AS subquery;

#Skewness
SELECT 
    (SUM(POWER(itemnetweight - (SELECT AVG(itemnetweight) FROM transaction), 3)) / 
    (COUNT(*) * POWER((SELECT STDDEV(itemnetweight) FROM transaction), 3))) AS skewness_itemnetweight
FROM transaction;

#-- Kurtosis
SELECT 
    ((SUM(POWER(itemnetweight - (SELECT AVG(itemnetweight) FROM transaction), 4)) / 
    (COUNT(*) * POWER((SELECT STDDEV(itemnetweight) FROM transaction), 4))) - 3) AS kurtosis_itemnetweight
FROM transaction;


select * from transaction;
#mean (quantity)
select avg(quantity) as avg_quantity from transaction;

#median
select quantity as median_quantity
from (
 SELECT quantity, ROW_NUMBER() OVER (ORDER BY quantity) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM transaction
) AS subquery
WHERE row_num = (total_count + 1) / 2 OR row_num = (total_count + 2) / 2;

#mode 
SELECT quantity AS mode_for_quantity
FROM (
    SELECT quantity, COUNT(*) AS frequency
    FROM transaction
    GROUP BY quantity
    ORDER BY count(*) DESC
    LIMIT 1
) AS subquery;

#Skewness
SELECT 
    (SUM(POWER(quantity - (SELECT AVG(quantity) FROM transaction), 3)) / 
    (COUNT(*) * POWER((SELECT STDDEV(quantity) FROM transaction), 3))) AS skewness_quantity
FROM transaction;

#-- Kurtosis
SELECT 
    ((SUM(POWER(quantity - (SELECT AVG(quantity) FROM transaction), 4)) / 
    (COUNT(*) * POWER((SELECT STDDEV(quantity) FROM transaction), 4))) - 3) AS kurtosis_quantity
FROM transaction;


select * from transaction;
#mean (rate)
select avg(rate) as avg_rate from transaction;

#median
select rate as median_rate
from (
 SELECT rate, ROW_NUMBER() OVER (ORDER BY rate) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM transaction
) AS subquery
WHERE row_num = (total_count + 1) / 2 OR row_num = (total_count + 2) / 2;

#mode 
SELECT rate AS mode_for_rate
FROM (
    SELECT rate, COUNT(*) AS frequency
    FROM transaction
    GROUP BY rate
    ORDER BY count(*) DESC
    LIMIT 1
) AS subquery;

#Skewness
SELECT 
    (SUM(POWER(rate - (SELECT AVG(rate) FROM transaction), 3)) / 
    (COUNT(*) * POWER((SELECT STDDEV(rate) FROM transaction), 3))) AS skewness_rate
FROM transaction;

#-- Kurtosis
SELECT 
    ((SUM(POWER(rate - (SELECT AVG(rate) FROM transaction), 4)) / 
    (COUNT(*) * POWER((SELECT STDDEV(rate) FROM transaction), 4))) - 3) AS kurtosis_rate
FROM transaction;

select * from transaction;
#mean
select avg(invoicequantity) as avg_rate from transaction;

#median
select invoicequantity as median_invoicequantity
from (
 SELECT invoicequantity, ROW_NUMBER() OVER (ORDER BY invoicequantity) AS row_num,
           COUNT(*) OVER () AS total_count
    FROM transaction
) AS subquery
WHERE row_num = (total_count + 1) / 2 OR row_num = (total_count + 2) / 2;

#mode 
SELECT invoicequantity AS mode_for_invoicequantity
FROM (
    SELECT invoicequantity, COUNT(*) AS frequency
    FROM transaction
    GROUP BY invoicequantity
    ORDER BY count(*) DESC
    LIMIT 1
) AS subquery;

#Skewness
SELECT 
    (SUM(POWER(invoicequantity - (SELECT AVG(invoicequantity) FROM transaction), 3)) / 
    (COUNT(*) * POWER((SELECT STDDEV(invoicequantity) FROM transaction), 3))) AS skewness_invoicequantity
FROM transaction;

#-- Kurtosis
SELECT 
    ((SUM(POWER(invoicequantity - (SELECT AVG(invoicequantity) FROM transaction), 4)) / 
    (COUNT(*) * POWER((SELECT STDDEV(invoicequantity) FROM transaction), 4))) - 3) AS kurtosis_invoicequantity
FROM transaction;

drop table transaction;
