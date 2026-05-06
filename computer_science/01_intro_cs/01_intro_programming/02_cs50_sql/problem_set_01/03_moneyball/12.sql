   SELECT "first_name",
          "last_name"
     FROM (SELECT "first_name",
                  "last_name",
                  "salary" / "H" AS 'dollars per hit'
             FROM "players"
             JOIN "salaries"
               ON "players"."id" = "salaries"."player_id"
             JOIN "performances"
               ON "players"."id" = "performances"."player_id"
              AND "salaries"."year" = "performances"."year"
            WHERE "salaries"."year" = 2001
              AND "H" <> 0
            ORDER BY "dollars per hit",
                  "first_name",
                  "last_name"
            LIMIT 10)
INTERSECT
   SELECT "first_name",
          "last_name"
     FROM (SELECT "first_name",
                  "last_name",
                  "salary" / "RBI" AS 'dollars per runs batted in'
             FROM "players"
             JOIN "salaries"
               ON "players"."id" = "salaries"."player_id"
             JOIN "performances"
               ON "players"."id" = "performances"."player_id"
              AND "salaries"."year" = "performances"."year"
            WHERE "salaries"."year" = 2001
              AND "RBI" <> 0
            ORDER BY "dollars per runs batted in",
                  "first_name",
                  "last_name"
            LIMIT 10)
    ORDER BY "last_name"
;
