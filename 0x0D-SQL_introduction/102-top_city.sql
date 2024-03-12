-- DISPLAY TOP 3 CITIES TEMPERATURE DURING july AND aUGUST ORDERED BY TEMP DESCCENDING
SELECT `city`, AVG('value') AS `avg`
FROM `temperatures`
WHERE `month` = 7 OR month = 8
GROUP BY `city`
ORDER BY `avg` DESC
LIMIT 3;