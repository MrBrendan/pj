import time
"""CREATE DATABASE dbname TEMPLATE=template0 ENCODING 'UTF-8' LC_COLLATE 'ru_RU.UTF-8' LC_CTYPE 'ru_RU.UTF-8';
CREATE TABLE alll(
id int primary key,
product varchar(255),
price varchar(15),
sale varchar(15),
date varchar (15),
shop varchar (52),
region varchar (52))
CREATE SEQUENCE user_id_seq;
ALTER TABLE user ALTER user_id SET DEFAULT NEXTVAL('user_id_seq');

Удалить все данные с таблицы (включая обновление инкремента):

TRUNCATE TABLE alll;
ALTER SEQUENCE id_seq RESTART;
UPDATE alll SET idd = DEFAULT;"""
