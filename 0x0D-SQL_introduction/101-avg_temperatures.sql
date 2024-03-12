-- display average temp by city ordered by temp descending
SELECT `city` , AVG(`value`) as `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg` DESC;