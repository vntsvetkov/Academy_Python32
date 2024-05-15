-- удаление таблицы из БД при условии, что она существует
DROP TABLE IF EXISTS mobile_devices;

-- создание таблицы при условии, что такой еще не существует
CREATE TABLE IF NOT EXISTS mobile_devices
(
	mobile_device_id SERIAL,
	device_os VARCHAR(10) NOT NULL,
	device_name VARCHAR(30) NOT NULL,
	model VARCHAR(30) NOT NULL,
	memory INTEGER NOT NULL,
	price NUMERIC(8, 2) NOT NULL DEFAULT 0,
	release_date DATE NOT NULL DEFAULT CURRENT_DATE,
	CONSTRAINT md_id PRIMARY KEY(mobile_device_id),
	CONSTRAINT md_memory_price_check CHECK(memory > 0 AND price >= 0)
);


-- Запрос на вставку трех записей в таблицу
INSERT INTO mobile_devices(device_os, device_name, model, memory, price, release_date)
VALUES
('Android', 'Tecno', 'Tecno Spark 6 Go', 64, 9999.99, '2023-05-24'),
('IOS', 'IPhone', '15 Pro', 256, 100000.00, '2023-07-05'),
('Symbian', 'Nokia', 'Nokia 5250', 1, 9500.00, '2023-08-29');


-- Добавим в таблицу еще один столбец counter - количество экземпляров определенной модели

ALTER TABLE mobile_devices 
ADD COLUMN counter INTEGER NOT NULL DEFAULT 0 CHECK(counter >= 0);

-- Каждой записи таблицы присвоим значение в поле counter равное 1

UPDATE mobile_devices
SET counter = 1

-- Запросы данных
-- Запрос 1. Получить все записи из таблицы

SELECT *
FROM mobile_devices

-- Запрос 2. Получить только поля model и price записи из таблицы, где поле device_os содержит Android или IOS
SELECT model AS "Модель", price AS "Цена" 
FROM mobile_devices
WHERE device_os = 'Android' OR device_os = 'IOS'

-- Запрос 3. Получить поля model, price, counter и составное поле "Итого", как результат умножения price и counter

SELECT 
	model AS "Модель", 
	price AS "Цена", 
	counter AS "Количество", 
	price * counter AS "Итого"
FROM 
	mobile_devices
WHERE 
	device_os = 'Android' AND
	device_os = 'IOS'


