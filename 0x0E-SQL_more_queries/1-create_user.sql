-- create user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- grant all privilege
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
-- reload grant table
FLUSH PRIVILEGES;
