SELECT 
    ph.first_name,
    ph.last_name
FROM (
    SELECT 
        pl.first_name,
        pl.last_name,
        s.salary / pe.H AS 'dollars per hit'
    FROM players pl
    JOIN salaries s
        ON pl.id = s.player_id
    JOIN performances pe
        ON pl.id = pe.player_id
        AND s.year = pe.year
    WHERE 
        s.year = 2001
        AND pe.H <> 0
    ORDER BY 
        "dollars per hit",
        pl.first_name,
        pl.last_name
    LIMIT 10
) ph

INTERSECT

SELECT 
    pr.first_name,
    pr.last_name
FROM (
    SELECT 
        pl.first_name,
        pl.last_name,
        s.salary / pe.RBI AS 'dollars per runs batted in'
    FROM players pl
    JOIN salaries s
        ON pl.id = s.player_id
    JOIN performances pe
        ON pl.id = pe.player_id
        AND s.year = pe.year
    WHERE 
        s.year = 2001
        AND pe.RBI <> 0
    ORDER BY 
        "dollars per runs batted in",
        pl.first_name,
        pl.last_name
    LIMIT 10
) pr

ORDER BY last_name
;
