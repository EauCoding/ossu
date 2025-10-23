-- -- Write a SQL query to list the titles and topics of all episodes teaching data or analysis.
SELECT 
    "title", 
    "topic"
FROM "episodes"
WHERE 
    "topic" LIKE '%data%' 
    OR "topic" LIKE '%analysis%'
;
