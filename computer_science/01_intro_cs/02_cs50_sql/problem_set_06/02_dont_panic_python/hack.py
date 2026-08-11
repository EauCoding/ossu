import sqlite3

conn = sqlite3.connect("ddont-panic.db")
cur = conn.cursor()

password = input("Enter a password: ")
cur.execute(
    """
    UPDATE "users"
    SET "password" = ?
    WHERE "username" = 'admin'
    ;
    """,
    password
)

cur.close()
conn.close()