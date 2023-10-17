-- Displays the 3 cities with the highest average temperatures between July and August.
SELECT `city`, AVG(`value`) AS `average_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `average_temp` DESC
LIMIT 3;
