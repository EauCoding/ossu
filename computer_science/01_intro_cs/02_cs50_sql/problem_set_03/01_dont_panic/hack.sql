-- Add false data to throw others off your trail. In particular, to frame emily33,
-- make it only appear—in the user_logs table—as if the admin account has had its password changed to emily33’s password.
INSERT INTO USER_LOGS (
    TYPE, 
    OLD_USERNAME, 
    NEW_USERNAME, 
    OLD_PASSWORD, 
    NEW_PASSWORD
)
SELECT 
    'update', 
    'admin', 
    'admin', 
    (
        SELECT PASSWORD
        FROM USERS
        WHERE USERNAME = 'admin'
    ), 
    (
        SELECT PASSWORD
        FROM USERS
        WHERE USERNAME = 'emily33'
    )
;

-- Alter the password of the website’s administrative account, admin, to instead be “oops!”.
UPDATE USERS
SET PASSWORD = 'oops!'
WHERE USERNAME = 'admin'
;

-- Erase any logs of the above password change recorded by the database.
DELETE FROM USER_LOGS
WHERE 
    OLD_USERNAME = 'admin'
    AND NEW_PASSWORD = 'oops!'
;
