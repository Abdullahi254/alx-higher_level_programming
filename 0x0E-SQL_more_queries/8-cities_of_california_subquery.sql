-- list all the cities of carlifornia
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California');
