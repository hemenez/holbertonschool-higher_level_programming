-- Script creates a table called first_table in current database
-- first_table contains an id and a name
-- If first_table already exists, script won't fail
CREATE TABLE IF NOT EXISTS first_table (id INT NOT NULL, name VARCHAR(256));
