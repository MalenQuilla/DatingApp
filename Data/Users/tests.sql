DROP database IF EXISTS test;
CREATE database IF NOT EXISTS test;
USE test;

CREATE TABLE Photo(
image LONGBLOB NOT NULL
);

SELECT * from Photo;