-- Write a SQL query to find the name and score of the top scorer in the second_table.
select score, name 
from second_table 
order by score desc;