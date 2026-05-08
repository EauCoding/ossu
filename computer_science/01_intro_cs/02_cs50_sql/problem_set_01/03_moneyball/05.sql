SELECT DISTINCT t.name
FROM performances pe
JOIN players pl
    ON pe.player_id = pl.id
JOIN teams t
    ON pe.team_id = t.id
WHERE 
    pl.first_name = 'Satchel'
    AND pl.last_name = 'Paige'
ORDER BY pl.last_name
;
