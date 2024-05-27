INSERT INTO mobile_devices(device_os, device_name, model, memory, price, release_date)
VALUES
('Android', 'Samsung', 'A52', 128, 39999.99, '2023-05-24'),
('IOS', 'IPhone', '14 Pro', 256, 120000.00, '2023-07-05'),
('Android', 'Samsung', 'A53', 128, 29500.00, '2023-08-29');



/* Удалить запись по признаку */

DELETE FROM mobile_devices
WHERE counter = 0;

/* Обновить по признаку */

UPDATE mobile_devices
SET counter = counter + 1
WHERE device_os = 'Android';

/* Обновить стоимость моделей Andoid и iOS*/
UPDATE mobile_devices
SET price = CASE
        WHEN device_os = 'Android' THEN price * 1.1
        WHEN device_os = 'IOS' THEN price * 1.3
            END
WHERE device_os in ('Android', 'IOS')

/* Запрос 1. Модели с какими ОС продаются ?*/

SELECT DISTINCT device_os
FROM mobile_devices

/* Запрос 2. Какие есть модели на 64, 128 или 256 ГБ памяти*/

SELECT *
FROM mobile_devices
WHERE memory in (64, 128, 256)

/* Запрос 3. Какие есть модели в ценовом диапазоне*/

SELECT *
FROM mobile_devices
WHERE price BETWEEN 10000 AND 50000

/* Запрос 4. Найти все модели Samsung серии A */

SELECT *
FROM mobile_devices
WHERE device_name = 'Samsung' AND model LIKE "A%"

/* Запрос 5. Найти все IPhone Pro */

SELECT *
FROM mobile_devices
WHERE device_name = 'IPhone' AND model LIKE "%Pro%"

/* Запрос 5. Узнать сколько месяцев прошло от даты релиза*/

SELECT 
    device_name, model, 
    extract(year from age(current_date, release_date)) AS "Year",
    extract(month from age(current_date, release_date)) AS "Month",
    extract(day from age(current_date, release_date)) AS "Month",

FROM mobile_devices

/* Запрос 6. Узнать в каком году вышла каждая модель на IOS*/

SELECT 
    device_name, 
    model, 
    extract(year from release_date)
FROM 
    mobile_devices
WHERE 
    device_os = 'IOS'

SELECT 
    device_name, 
    model, 
    substring(CAST(release_date AS VARCHAR), from 1 for 4)
FROM 
    mobile_devices
WHERE 
    device_os = 'IOS'


SELECT 
    device_name, 
    model, 
    substring(release_date :: VARCHAR from 1 for 4)
FROM 
    mobile_devices
WHERE 
    device_os = 'IOS'