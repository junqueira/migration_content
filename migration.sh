#!/usr/bin/env bash
sudo mysql
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON * . * TO 'admin'@'localhost';
FLUSH PRIVILEGES;
quit

mysql --host=localhost --user=admin --password=admin
use new_schema
show tables;
CREATE TABLE IF NOT EXISTS content (
	id INT(5) AUTO_INCREMENT PRIMARY KEY,
	titulo VARCHAR(50) NOT NULL,
    descricao  VARCHAR(100) NOT NULL,
    texto  VARCHAR(200) NOT NULL,
    data  DATE )ENGINE=MyISAM;