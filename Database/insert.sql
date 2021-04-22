--inserts files into db

DROP TABLE if EXISTS User;

CREATE TABLE User (
	username varchar(255) PRIMARY KEY UNIQUE NOT NULL,
	email varchar(255),
	password varchar(255)
);

insert into User values(
    "wmigdol",
    "will.migdol@gmail.com",
    "password123"
);