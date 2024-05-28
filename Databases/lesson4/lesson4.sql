/*

AVG - cреднее значение выражения
COUNT - возвращает количество выражений
MAX - максимальное значение выражения
MIN - минимальное значение выражения
SUM - суммированное значение выражения

Используются вместе с группировкой GROUP BY / HAVING

*/

SELECT AVG(price) AS "Средняя цена"
FROM mobile_devices

SELECT COUNT(counter) AS "Количество моделей"
FROM mobile_devices
WHERE device_os = 'Android'

SELECT MAX(price) AS "Наибольшая стоимость"
FROM mobile_devices

SELECT SUM(price * counter) AS "Итоговая стоимость"
FROM mobile_devices


/* Запрос 1. Сгрупировать записи таблицы по ОС и определить
количество через COUNT*/

SELECT 
	device_os, 
	COUNT(*),
	SUM(counter) AS "Количество"
FROM mobile_devices
GROUP BY device_os

/*Запрос 2. Сгруппировать записи по ОС и модели + количество*/

SELECT 
	device_os,
    device_name,
	COUNT(*),
FROM mobile_devices
GROUP BY device_os, device_name

/* Запрос 3. Извлечь из запроса 2 только те группы, где 
количество больше 2*/

SELECT 
	device_os,
    device_name,
	COUNT(*) AS "Количество"
FROM mobile_devices
GROUP BY device_os, device_name
HAVING COUNT(*) > 2

/* Запрос 4. В запросе 3 группировать только модели где 
количество на складе больше 0*/

SELECT 
	device_os,
    device_name,
	COUNT(*) AS "Количество"
FROM mobile_devices
WHERE counter > 0
GROUP BY device_os, device_name
HAVING COUNT(*) > 2

/* Запрос 5. В запросе 3 группировать только модели, которые
вышли в 2023 году*/

SELECT 
	device_os,
    device_name,
	COUNT(*) AS "Количество",
	ROUND(AVG(price), 2) AS "Средняя стоимость"
FROM mobile_devices
WHERE extract(year from release_date) = 2023
GROUP BY device_os, device_name
HAVING COUNT(*) > 1

/* Запрос 6. Запросить среднюю стоимость по каждой ОС, где
количество на складе больше 0*/

SELECT device_os, AVG(price) AS "Средняя стоимость"
FROM mobile_devices
WHERE counter > 0
GROUP BY device_os

/* Запрос 7. Максимальная стоимость Iphone Pro, 
который есть на складе*/

SELECT 
    device_name, 
    model, 
    MAX(price) AS "Максимальная стоимость"
FROM 
    mobile_devices
WHERE 
    counter > 0 AND 
    model LIKE '%Pro%'AND 
    device_name = 'IPhone'
GROUP BY 
    device_name, model
HAVING MAX(price) = (SELECT MAX(price)
                     FROM mobile_devices
                     WHERE device_name = 'IPhone' AND counter > 0)

/* Запрос 8. Запросить общую стоимость всех IOS и Android
моделей, которые есть на складе*/

SELECT device_os, SUM(price) AS "Общая стоимость"
FROM mobile_devices
WHERE counter > 0 AND device_os in ('IOS', 'Android')
GROUP BY device_os

/* Запрос 9. Максимальная стоимость Iphone Pro, 
который есть на складе*/

SELECT 
    device_name, 
    model, 
    MAX(price) AS total_price
FROM 
    mobile_devices
WHERE 
    counter > 0 AND 
    model LIKE '%Pro%'AND 
    device_name = 'IPhone'
GROUP BY 
    device_name, model
ORDER BY total_price DESC
LIMIT 1

/* Запрос 10. Запрос 9, но вторая по стоимости модель*/

SELECT 
    device_name, 
    model, 
    MAX(price) AS total_price
FROM 
    mobile_devices
WHERE 
    counter > 0 AND 
    model LIKE '%Pro%'AND 
    device_name = 'IPhone'
GROUP BY 
    device_name, model
ORDER BY total_price DESC
LIMIT 1
OFFSET 1