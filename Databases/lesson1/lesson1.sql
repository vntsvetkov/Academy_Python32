CREATE TABLE IF NOT EXISTS customers (
	customer_id SERIAL PRIMARY KEY,
	first_name VARCHAR(30) NOT NULL CHECK(LENGTH(first_name) > 0) DEFAULT 'Неизвестно',
	last_name VARCHAR(50) NOT NULL CHECK(LENGTH(first_name) > 0) DEFAULT 'Неизвестно',
	age INTEGER NOT NULL CHECK(age > 0),
	phone VARCHAR(15) NOT NULL UNIQUE,
	email TEXT NOT NULL UNIQUE,
	inn VARCHAR(13) NOT NULL CHECK(LENGTH(first_name) > 0) UNIQUE
);
