-- In this task, you are asked to update the score of a specific person in the second_table.
SELECT score, name
FROM second_table
UPDATE second_table
SET score = 10
WHERE name = 'Bob';