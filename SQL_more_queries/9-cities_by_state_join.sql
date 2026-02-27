-- Write a SQL query that lists all the cities in the database, including the state they belong to. The results should be sorted by city id in ascending order.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;