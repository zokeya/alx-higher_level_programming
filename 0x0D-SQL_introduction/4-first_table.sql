--creates a table called first_table in the current database
USE `database_name`;
CREATE TABLE IF NOT EXISTS `first_table` (
	id INT,
	name VARCHAR(256)
	) ENGINE=INNODB;
