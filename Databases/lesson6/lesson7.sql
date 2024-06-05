
CREATE TABLE Faculties
(
    faculty_id SERIAL PRIMARY KEY,
    faculty_name VARCHAR(100) NOT NULL UNIQUE
    CONSTRAINT check_name CHECK(LENGTH(faculty_name) > 0)
);

CREATE TABLE Departments
(
    department_id SERIAL PRIMARY KEY,
    building INTEGER NOT NULL CHECK(building >= 1 AND building <= 5),
    financing NUMERIC(15,2) NOT NULL DEFAULT 0 CHECK(financing > 0),
    department_name VARCHAR(100) NOT NULL UNIQUE CHECK(LENGTH(department_name) > 0),
    faculty_id INTEGER NOT NULL,
    FOREIGN KEY(faculty_id)
        REFERENCES Faculties(faculty_id)
            ON DELETE CASCADE
);

CREATE TABLE Groups
(
    group_id SERIAL PRIMARY KEY,
    group_name VARCHAR(10) NOT NULL UNIQUE CHECK(LENGTH(group_name) > 0),
    course INTEGER NOT NULL CHECK(course >= 1 AND course <= 5),
    department_id INTEGER,
    FOREIGN KEY(department_id)
        REFERENCES Faculties(department_id)
            ON DELETE SET NULL
);


/*
Вывести названия групп 5-го курса кафедры Software Development

*/

SELECT 
    group_name,
    course
FROM
    Groups
INNER JOIN
    Departments
ON
    Groups.department_id = Departments.department_id AND
    Departments.department_name = 'Software Development' AND
    Groups.course = 5

