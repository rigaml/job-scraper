----------------
-- Few queries that can be useful to inspect the data
----------------

----------------
-- Selects jobs inserted from a particular date.
SELECT *
  FROM job
WHERE created_at > '2024-05-22';
----------------

----------------
-- Deletes jobs inserted from a particular date.
-- Remove the lines "BEGIN TRANSACTION" and "ROLLBACK" when you are sure want to execute statement.
----------------
BEGIN TRANSACTION;
DELETE FROM job
WHERE created_at > '2024-05-22';
ROLLBACK;