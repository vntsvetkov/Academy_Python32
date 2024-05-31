/*
Нормализация БД. Типы связей БД.

1 тип. Один ко одному

Пользователь (владелец) - паспорт

2 тип. Один ко многим

Пользователь (владелец) - номер телефона

Users
user_id     name 
1           Иван    
2           Петр

Phones
phone_id    phone       user_id (Внешний ключ)
1           56-85-69    1
2           89-65-35    1
3           65-86-33    2

3 тип. Многие ко многим

Goods
good_id     name    cost  
1           Стол    10000

Clients
client_id   name    pasport_id
1           Иван    1

Pasports
pasport_id  series  number
1           20 54   457812

Phones
phone_id    phone       client_id (Внешний ключ)
1           56-85-69    1
2           89-65-35    1
3           65-86-33    2

Orders
order_id    client_id   good_id  order_date
1           1           1        
2           1           2
3           2           1


*/

CREATE TABLE IF NOT EXISTS Goods
(
    good_id SERIAL PRIMARY KEY,
    good_name VARCHAR(50) NOT NULL,
    cost NUMERIC(5,2) NOT NULL CHECK(cost >= 0)
);

CREATE TABLE IF NOT EXISTS Clients
(
    client_id SERIAL PRIMARY KEY,
    full_name VARCHAR(50) NOT NULL,
    pasport_id INTEGER UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Pasports
(
    pasport_id SERIAL PRIMARY KEY,
    series VARCHAR(4) NOT NULL, 
    pas_number VARCHAR(6) NOT NULL
);

CREATE TABLE IF NOT EXISTS Phones
(
    phone_id SERIAL PRIMARY KEY,
    phone TEXT UNIQUE NOT NULL,
    client_id INTEGER,
    FOREIGN KEY(client_id) 
        REFERENCES Clients(client_id)
            ON DELETE SET NULL

);

CREATE TABLE IF NOT EXISTS Orders
(
    order_id SERIAL PRIMARY KEY,
    client_id INTEGER,
    good_id INTEGER,
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(client_id) 
        REFERENCES Clients(client_id)
            ON DELETE SET NULL,
    FOREIGN KEY(good_id) 
        REFERENCES Goods(good_id)
            ON DELETE SET NULL
);


INSERT INTO Goods(good_name, cost)
VALUES('Стол', 900.00);

INSERT INTO Clients(full_name, pasport_id)
VALUES('Иван', 1);

INSERT INTO Pasports(series, pas_number)
VALUES('4567', '123456');

INSERT INTO Phones(phone, client_id)
VALUES('45-67-89', 1);

INSERT INTO Orders(client_id, good_id)
VALUES(1, 1)
