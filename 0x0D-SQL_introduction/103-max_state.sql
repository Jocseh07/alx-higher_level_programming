-- display the mx temp of each state ordered by state name
SELECT `state`, MAX(`value`) AS `max`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;