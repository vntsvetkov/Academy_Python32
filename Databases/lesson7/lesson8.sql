/*

Подзапросы и CTE (предзапрос)

Что может вернуть подзапрос:
    - Значение
    - Столбец значений
    - Таблицу (для этого чаще используют СTE)




*/

/*
Где применять:
    - WHERE, HAVING

    Запрос 1. Показать устройства, стоимость 
    которых выше средней стоимости всех товаров

*/
    SELECT 
        *
    FROM 
        mobile_devices
    WHERE 
        price > (SELECT 
                    AVG(price) 
                 FROM
                    mobile_devices)


/*
Запрос 2. Найти все устройства стоимостью
между самой дорогой и самой дешевой моделью Iphone Pro

*/

    SELECT *
    FROM mobile_devices
    WHERE device_name = 'Iphone' AND 
          model LIKE '%Pro%' AND
          price BETWEEN (SELECT MIN(price)
                         FROM mobile_devices
                         WHERE device_name = 'Iphone' AND
                               model LIKE '%Pro%') AND 
                        (SELECT MAX(price)
                         FROM mobile_devices
                         WHERE device_name = 'Iphone' AND
                               model LIKE '%Pro%')
    

/*
    - INSERT, DELETE, UPDATE/SET

Запрос 3. Удалить из таблицы все Iphone
стоимость которых ниже средней стоимости этих 
моделей

*/
    DELETE FROM mobile_devices
    WHERE device_name = 'IPhone' AND 
          price < (SELECT AVG(price)
                   FROM mobile_devices
                   WHERE device_name = 'IPhone')

/*
Запрос 4. Увеличить стоимость каждой модели
Samsung на 10% от минимальной стоимости этих моделей
*/

    UPDATE mobile_devices
    SET price = price + 0.1 * (SELECT MIN(price)
                         FROM mobile_devices
                         WHERE device_name = 'Samsung')
    WHERE device_name = 'Samsung'


/*
    - FROM (получить табличку)

    Запрос 5. 

*/

    SELECT d_name, model, total
    FROM (SELECT mobile_device_id AS mb_id, 
                device_name AS d_name,
                model,
                price * counter AS total
         FROM mobile_devices) AS mod_dev
    WHERE total > 100000
    

/*
    - SELECT (получить столбец или таблицу)

    Таблица Клиенты и паспорта
    Запрос 6. Запросить данные паспорта и имя его владельца
*/

    SELECT series, 
           pas_number,
           (SELECT full_name
            FROM Clients
            WHERE Pasports.pasport_id = Clients.pasport_id)

    FROM Pasports




WITH min_price AS 
(
    SELECT MIN(price)
    FROM mobile_devices
    WHERE device_name = 'Iphone' AND
          model LIKE '%Pro%'
),
max_price AS 
(
    SELECT MAX(price)
    FROM mobile_devices
    WHERE device_name = 'Iphone' AND
          model LIKE '%Pro%'
)
SELECT *
FROM mobile_devices
WHERE device_name = 'Iphone' AND 
      model LIKE '%Pro%' AND
      price BETWEEN min_price AND max_price



/*

Запрос 7. Показать все покупки клиента по паспортным данным

Имя клинета, что купил, стоимость товара, когда


*/

WITH cur_client_id AS 
(
    SELECT client_id
    FROM Clients
    WHERE Clients.pasport_id = (SELECT pasport_id
                                FROM Pasports
                                WHERE series = '4567' AND
                                pas_number = '123456')
)
SELECT 
    Clients.full_name,
    Goods.good_name,
    Goods.cost,
    Orders.order_date
FROM Clients, Goods, Orders
WHERE Clients.client_id = (
				SELECT client_id 
				FROM cur_client_id) AND
      Clients.client_id = Orders.client_id AND
      Orders.good_id = Goods.good_id