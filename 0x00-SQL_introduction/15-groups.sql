-- lists number of records with same score in table
SELECT NAME, count( * ) as SCORE FROM 'first_table' GROUP BY NAME;
