

SELECT 
    name, 
    phone
FROM 
    Phones
INNER JOIN 
    Clients
ON Clients.client_id = Phones.client_id

/*
Clients
client_id   name    pasport_id
1           Иван    1

Phones
phone_id    phone       client_id (Внешний ключ)
1           56-85-69    1
2           89-65-35    1
3           65-86-33    2


name    phone
Иван    56-85-69 
Иван    89-65-35
NULL    65-86-33

*/

SELECT 
    Clients.full_name, 
    Phones.phone,
	Pasports.series,
	Pasports.pas_number
FROM
    Phones
INNER JOIN 
    Clients
ON 
	Clients.client_id = Phones.client_id
INNER JOIN 
	Pasports
ON 
	Clients.pasport_id = Pasports.pasport_id



SELECT 
    Clients.full_name, 
    Phones.phone,
    Pasports.series,
	Pasports.pas_number
FROM
    Phones,
    Clients,
    Pasports
WHERE
	Clients.client_id = Phones.client_id AND
    Clients.pasport_id = Pasports.pasport_id


SELECT 
    Clients.full_name,
	Pasports.series,
	Pasports.pas_number
FROM
    Clients
LEFT JOIN 
	Pasports
ON 
	Clients.pasport_id = Pasports.pasport_id




WHERE Pasports.series IS NOT NULL AND
      Pasports.pas_number IS NOT NULL