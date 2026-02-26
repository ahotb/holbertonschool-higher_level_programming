--	Create a table named unique_id with the following columns:
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name varchar(256) NOT NULL
);