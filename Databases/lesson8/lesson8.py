import psycopg2

"""
Транзакции.
1. Группировка одной или нескольких операций с БД.

Пример: БД Магазин
Таблица "Мобильные устройства" в нашем магазине
Таблица "Мобильные устройства" в другом магазине 

Задача: переместить одно устройство из первой таблицы во вторую

Найти Iphone 15 Pro
Уменьшить количество моделей на N единиц в первой таблице

    UPDATE mobile_devices_shop_1
    SET counter = counter - N
    WHERE device_name = 'Iphone' AND model = '15 Pro'

Увеличить количество моделей на N единиц во второй таблице

    UPDATE mobile_devices_shop_2
    SET counter = counter + N
    WHERE device_name = 'Iphone' AND model = '15 Pro'


Обеспечивает согласованность данных
Гарантирует выполнение либо всех операций либо ни одной

Команды TCL: BEGIN, COMMIT, ROLLBACK.

Транзакции выполняются внутри одного соединения.

"""

# Создать соединение с БД

"""
Методы объекта соединения
close() - закрыть соединение
cursor() - создет объект для запросов

    

commit() - подтверждение транзакции
rollback() - принудительно завершить транзакцию

"""
connection = None
cursor = None
try:
    connection = psycopg2.connect(dbname='shop',
                                  host='localhost',
                                  port=5432,
                                  user='postgres',
                                  password='postgres')
except psycopg2.Error as e:
    print(e)
else:
    print('Соединение установлено')
    cursor = connection.cursor()
    # query = """SELECT * FROM mobile_devices ORDER BY mobile_device_id"""
    params = ('Android', 'Samsung', 'A60', 256, 85000.00, '2024-05-24', 2)
    query = """ INSERT INTO mobile_devices(device_os, device_name, model, memory, price, release_date, counter)
                VALUES (%s, %s, %s, %s, %s, %s, %s)"""

    params_many = [(1,), (2,)]

    try:
        cursor.execute(query, params)
    except psycopg2.Error as e:
        print(e)
    else:
        print("Данные успешно добавлены")

    query = """SELECT 
                    device_name, 
                    model, 
                    extract(year from release_date)::INTEGER
                FROM 
                    mobile_devices
                WHERE 
                    device_os = %s AND model LIKE %s """
    params = ('IOS', "%Pro%")
    try:
        cursor.execute(query, params)
    except psycopg2.Error as e:
        print(e)
    else:
        for row in cursor:
            print(row)

finally:
    if connection:
        cursor.close()
        # connection.commit()
        connection.close()

