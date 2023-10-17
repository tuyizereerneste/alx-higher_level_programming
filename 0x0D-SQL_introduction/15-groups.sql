-- Lists the number of records with the same score in the second_table in my MySQL server.
-- Records are count ordered by descending order.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
