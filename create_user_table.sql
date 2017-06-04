CREATE TABLE User
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(30) NOT NULL,
    passoword VARCHAR(30) NOT NULL
);
CREATE UNIQUE INDEX User_username_uindex ON User (username);

CREATE TABLE Todo
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner INT NOT NULL,
    status VARCHAR(10) NOT NULL,
    due_date DATETIME,
    description VARCHAR(1000),
    CONSTRAINT owner FOREIGN KEY (id) REFERENCES User (id)
);