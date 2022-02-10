-- lists all cities of California in database hbtn_0d_usa
SELECT id, name FROM cities WHERE states.name == 'California'
ORDER BY cities.id ASC;
