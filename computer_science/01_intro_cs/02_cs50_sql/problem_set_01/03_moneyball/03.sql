SELECT 
    pe.year,
    pe.HR
FROM performances pe
JOIN players pl
    ON pe.player_id = pl.id
WHERE 
    pl.first_name = 'Ken'
    AND pl.last_name = 'Griffey'
    AND pl.birth_year = 1969
ORDER BY pe.year DESC
;
