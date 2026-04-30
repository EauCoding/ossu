SELECT DISTINCT 
    "birth_city" AS 'Home Town', 
    "birth_state" AS 'Home State', 
    "birth_country" AS 'Home Country'
FROM "players"
WHERE "birth_country" <> 'USA'
ORDER BY 
    "birth_country", 
    "birth_city", 
    "birth_state"
;
