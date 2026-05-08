SELECT 
    pl.first_name,
    pl.last_name,
    s.salary,
    pe.HR,
    s.year
FROM players pl
JOIN salaries s
    ON pl.id = s.player_id
JOIN performances pe
    ON pl.id = pe.player_id
    AND s.year = pe.year
ORDER BY 
    pl.id,
    s.year DESC,
    pe.HR DESC,
    s.salary DESC
;
