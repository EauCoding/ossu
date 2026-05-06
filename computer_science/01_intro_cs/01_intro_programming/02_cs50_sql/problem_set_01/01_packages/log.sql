-- *** The Lost Letter ***
SELECT 
	'At what type of address did the Lost Letter end up?' AS 'Questions',
    type AS 'Answers'
FROM addresses
WHERE id = (
	SELECT to_address_id
    FROM packages
    WHERE 
		from_address_id = (
			SELECT id
			FROM addresses
			WHERE address = '900 Somerville Avenue'
		)
        AND "contents" = 'Congratulatory letter'
)

UNION

SELECT 
	'At what address did the Lost Letter end up?' AS 'Questions',
	address AS 'Answers'
FROM addresses
WHERE id = (
	SELECT to_address_id
    FROM packages
	WHERE 
		from_address_id = (
			SELECT id
        	FROM addresses
        	WHERE address = '900 Somerville Avenue'
		)
        AND contents = 'Congratulatory letter')

UNION

-- *** The Devious Delivery ***
SELECT 
	'At what type of address did the Devious Delivery end up?' AS 'Questions',
    type AS 'Answers'
FROM addresses
WHERE id = (
	SELECT address_id
    FROM scans
    WHERE 
		package_id = (
			SELECT id
            FROM packages
            WHERE from_address_id IS NULL
		)
        AND action = 'Drop'
)

UNION

SELECT 
	'What were the contents of the Devious Delivery?' AS 'Questions',
	contents AS 'Answers'
FROM packages
WHERE from_address_id IS NULL

UNION

-- *** The Forgotten Gift ***
SELECT 
	'What are the contents of the Forgotten Gift?' AS 'Questions',
    contents AS 'Answers'
FROM packages
WHERE from_address_id = (
	SELECT id
    FROM addresses
    WHERE address = '109 Tileston Street'
)

UNION

SELECT 
	'Who has the Forgotten Gift?' AS 'Questions',
    name AS 'Answers'
FROM drivers
WHERE id = (
	SELECT driver_id
    FROM scans
    WHERE package_id = (
		SELECT id
        FROM packages
        WHERE from_address_id = (
			SELECT id
            FROM addresses
            WHERE address = '109 Tileston Street'
		)
	)
	ORDER BY timestamp DESC
    LIMIT 1
)
;
