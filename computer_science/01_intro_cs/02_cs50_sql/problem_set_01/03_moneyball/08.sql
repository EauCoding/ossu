SELECT s.salary
FROM performances p
JOIN salaries s
    ON p.player_id = s.player_id
WHERE 
    p.year = 2001
    AND s.year = 2001
ORDER BY p.HR DESC
LIMIT 1
;
