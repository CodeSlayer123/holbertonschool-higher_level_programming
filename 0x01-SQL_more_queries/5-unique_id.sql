-- creates table unique_id on MySql server
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT(1) UNIQUE,
    name VARCHAR(256)
);
