-- CREATE DATABASE hbtn_0d_usa AND THE TABLE states IN DATABASE ON SERVER
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_NCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));