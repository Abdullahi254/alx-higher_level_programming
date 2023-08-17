-- creating databse hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- creating table cities in hbtn_0d_usa
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
name VARCHAR(256), state_id INT NOT NULL,  PRIMARY KEY (id), FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id));
