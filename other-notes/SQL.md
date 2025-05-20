# 2025-04-15 SQL - Notes

# 2025-04-14 SQL - Notes

## Databases
### Relational DBs
- SQL (Structured Query Language)
- Data is stored in a structured setup with tables/columns/rows
- Built and designed around relationships between tables
- Generally well organized ?!
- Querying is fast
- Duplication of data is minimal
### Non-relational DBs
- NoSQL
- Data is less Structured
- Built as a large Dataset, often stored as a document (e.g. big JSON)
- More flexible - useful when the shape of the data is unpredictable
- More Scalable
- Can be easier to store more complex (e.g. highly nested data)


### Postgres
- Database Management System
- The software that actually makes changes to the databases
- The thing we use to execute our SQL code
- Extends SQL's functionality
- Comes with `psql` *CLI*
#### `psql`

- when you get an output such as `INSERT 0 7` it means 0 deleted, 7 created

##### Flags
- `-H` html
- `-q` run quietly
- `-f` execute commands from file, then exit

## Conventions
- names all lowercase in snake_case
- table names in plural
- column names singular


## Foreign Keys
```sql
CREATE TABLE albums (
    album_id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    -- shorthand version for foreign key ref
    stock_id INT NOT NULL REFERENCES stock(stock_id), 
    release_year INT,
    artist_id INT,
    -- long hand version for foreign key ref
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);
```

## Joins
Just writing `JOIN` is shorthand for `INNER JOIN` in Postgres

## ERD
[ERDs](https://dbdiagram.io)

#### `psql` CLI Commands
- `\?` help 
- `\q` Quit 
- `\l` lists all our databases
- `\c database_name` connects us to a specific database
- `\dt` lists all schemas (tables)
#### `psql` with files
- `psql -f file_path`
### Delete Database:
`DROP DATABASE IF EXISTS nc_music`



## SQL Queries
- Columns are the attributes or properties of the table
### Select query for a specific column
```sql
-- Select query for a specific column
SELECT column, another_column, …
FROM mytable;
```
### Select query for all columns
```sql
-- Select query for all columns
SELECT * 
FROM mytable;
```
### Select query with constraints
```sql
-- Select query with constraints
SELECT column, another_column, …
FROM mytable
WHERE condition
    AND/OR another_condition
    AND/OR …;
```
### Select query with unique results
```sql
-- Select query with unique results
SELECT DISTINCT column, another_column, …
FROM mytable
WHERE condition(s);
```
### Select query with ordered results
```sql
-- Select query with ordered results
SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC;
```
### Select query with limited rows
```sql
-- Select query with limited rows
SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC
LIMIT num_limit OFFSET num_offset;
```
### Simple SELECT query
```sql
-- simple SELECT query
SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC
LIMIT num_limit OFFSET num_offset;
```

| Operator | Condition | SQL Example |
|:-:|---|---|
| =, !=, <, <=, >, >= | Standard numerical operators | col_name **!=** 4 |
| BETWEEN … AND … | Number is within range of two values (inclusive) | col_name **BETWEEN** 1.5 **AND** 10.5 |
| NOT BETWEEN … AND … | Number is not within range of two values (inclusive) | col_name **NOT BETWEEN** 1 **AND** 10 |
| IN (…) | Number exists in a list | col_name **IN** (2, 4, 6) |
| NOT IN (…) | Number does not exist in a list | col_name **NOT IN** (1, 3, 5) |

| Operator | Condition | Example |
|:-:|---|---|
| = | Case sensitive exact string comparison (**notice the single equals**) | col_name **=** "abc" |
| != or <> | Case sensitive exact string inequality comparison | col_name **!=** "abcd" |
| LIKE | Case insensitive exact string comparison | col_name **LIKE** "ABC" |
| NOT LIKE | Case insensitive exact string inequality comparison | col_name **NOT LIKE** "ABCD" |
| % | Used anywhere in a string to match a sequence of zero or more characters (only with LIKE or NOT LIKE) | col_name **LIKE** "%AT%"<br>(matches "~AT~", "~AT~TIC", "C~AT~" or even "B~AT~S") |
| _ | Used anywhere in a string to match a single character (only with LIKE or NOT LIKE) | col_name **LIKE** "AN_"<br>(matches "~AN~D", but not "~AN~") |
| IN (…) | String exists in a list | col_name **IN** ("A", "B", "C") |
| NOT IN (…) | String does not exist in a list | col_name **NOT IN** ("D", "E", "F") |

## Inserting Data
### Insert statement with values for all columns
```sql
-- Insert statement with values for all columns
INSERT INTO mytable
VALUES (value_or_expr, another_value_or_expr, …),
       (value_or_expr_2, another_value_or_expr_2, …),
       …;
```
### Insert statement with specific columns
```sql
-- Insert statement with specific columns
INSERT INTO mytable
(column, another_column, …)
VALUES (value_or_expr, another_value_or_expr, …),
      (value_or_expr_2, another_value_or_expr_2, …),
      …;
```
### Insert statement with expressions
```sql
-- Example Insert statement with expressions
INSERT INTO boxoffice
(movie_id, rating, sales_in_millions)
VALUES (1, 9.9, 283742034 / 1000000);
```

## Updating Data
In order not to make mistakes, a good idea is to first write a `SELECT` statement and get the `WHERE` clause right, run the query to make sure we are updating the correct data and only then write the rest of the `UPDATE` statement


### Update statement with values
``` sql
-- Update statement with values
UPDATE mytable
SET column = value_or_expr, 
    other_column = another_value_or_expr, 
    …
WHERE condition;
```
- When updating, there are no JOINS, you chain different WHERE statements after a FROM statement
- The FROM statement can make different pieces of data available for comparison and usage in the WHERE clause
```sql
UPDATE cats
    SET danger_rating = 10
WHERE cats.crime_id = cat_crimes.crime_id AND cat_crimes.crime_description LIKE 'Grand theft lasagne'
RETURNING *;
```


## Deleting Data
Again it's better to run a `SELECT` query first and get the `WHERE` clause right before
running the desired `DELETE` query.
```sql
-- Delete statement with condition
DELETE FROM mytable
WHERE condition;
```


## Creating Tables
### Create table statement with optional table constraint and default value
```sql
-- Create table statement w/ optional table constraint and default value
CREATE TABLE IF NOT EXISTS mytable (
    column DataType TableConstraint DEFAULT default_value,
    another_column DataType TableConstraint DEFAULT default_value,
    …
);
```
### Example Movies table schema
```sql
-- Movies table schema
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    director TEXT,
    year INTEGER, 
    length_minutes INTEGER
);
```

| Data type | Description |
|---|---|
| **INTEGER**, **BOOLEAN** | The integer datatypes can store whole integer values like the count of a number or an age. In some implementations, the boolean value is just represented as an integer value of just 0 or 1. |
| **FLOAT**, **DOUBLE**, **REAL** | The floating point datatypes can store more precise numerical data like measurements or fractional values. Different types can be used depending on the floating point precision required for that value. |
| **CHARACTER(num_chars)**, **VARCHAR(num_chars)**, **TEXT** | The text based datatypes can store strings and text in all sorts of locales. The distinction between the various types generally amount to underlaying efficiency of the database when working with these columns.<br>Both the CHARACTER and VARCHAR (variable character) types are specified with the max number of characters that they can store (longer values may be truncated), so can be more efficient to store and query with big tables. |
| **DATE**, **DATETIME** | SQL can also store date and time stamps to keep track of time series and event data. They can be tricky to work with especially when manipulating data across timezones. |
| **BLOB** | Finally, SQL can store binary data in blobs right in the database. These values are often opaque to the database, so you usually have to store them with the right metadata to requery them. |
| Docs: [MySQL](http://dev.mysql.com/doc/refman/5.6/en/data-types.html), [Postgres](http://www.postgresql.org/docs/9.4/static/datatype.html), [SQLite](https://www.sqlite.org/datatype3.html), [Microsoft SQL Server](https://msdn.microsoft.com/en-us/library/ms187752.aspx) |

### Table constrains (not comprehensive)
| Constraint | Description |
|---|---|
| **PRIMARY KEY** | This means that the values in this column are unique, and each value can be used to identify a single row in this table. |
| **AUTOINCREMENT** | For integer values, this means that the value is automatically filled in and incremented with each row insertion. Not supported in all databases. |
| **UNIQUE** | This means that the values in this column have to be unique, so you can't insert another row with the same value in this column as another row in the table. Differs from the `PRIMARY KEY` in that it doesn't have to be a key for a row in the table. |
| **NOT NULL** | This means that the inserted value can not be `NULL`. |
| **CHECK (expression)** | This allows you to run a more complex expression to test whether the values inserted are valid. For example, you can check that values are positive, or greater than a specific size, or start with a certain prefix, etc. |
| **FOREIGN KEY** | This is a consistency check which ensures that each value in this column corresponds to another value in a column in another table.<br><br>For example, if there are two tables, one listing all Employees by ID, and another listing their payroll information, the `FOREIGN KEY` can ensure that every row in the payroll table corresponds to a valid employee in the master Employee list. |



## SQL
### SQL Agregate functions
- AVG()
- COUNT()
- etc

### Groups
Generally speaking the thing you want to group by is the Primary Key
```sql
SELECT artists.artist_name, COUNT(albums.album_id) AS total_albums_released
FROM albums
RIGHT JOIN artists ON artists.artists_id = albums.artist_id
GROUP BY artists.artists_id
```

### Junction Tables
- To solve many to many relationships
- convention is the name of both tables eg.: `artists_genres`

```sql
CREATE TABLE IF NOT EXISTS artists_genres
artist_id INT REFERENCES artists(artist_id)
genre_id INT REFERENCES genre(genre_id)
PRIMARY KEY (artist_id, genre_id); -- composite primary key enforces uniqueness in this relationship
```
- composite primary keys do not create a column, they are only a table constraint

Querying all artists and their genres
```sql
SELECT artists.name, genres.genre
FROM artists
INNER JOIN artists_genres
ON artists.artist_id = artists_genres.artist_id
INNER JOIN genres
ON genres.genre_id = artists_genres.genre_id;
```

### `INTERSECT` method
Only things that exist in both tables

### `EXCEPT` method
Only things that only exist on the left table

### `CASE` statements
```sql
SELECT danger_rating,
    CASE
        WHEN danger_rating >= 9 THEN 'very dangerous'
        WHEN danger_rating <= 6 THEN 'not dangerous'
        ELSE 'dangerous'
        END how_dangerous --this is the new column alias
FROM bears;
```

## CASE
```sql
SELECT CASE
    WHEN is_identity_secret = TRUE THEN hero_name
    ELSE real_name
END AS hero
FROM superheroes;
```
## Sub Queries

```sql
SELECT * FROM superheroes
WHERE movie_appearances > (SELECT AVG(movie_appearances) FROM superheroes);
```
### Subquery Types
- Scalar
- Multi-row
- Correlated

## EXPLAIN ANALYZE
- before the query will gives us information about a
```sql
EXPLAIN ANALYSE SELECT * FROM customers WHERE fist_name = 'John';
```

## INDEX
```sql
CREATE INDEX index_arbitrary_name ON table_name(column_name);
```
```sql
DROP INDEX IF EXISTS index_arbitrary_name;
```

## Common Table Expressions
```sql
WITH superhero_team_sizes AS (
    SELECT count(superheroes.team_id) AS hero_count FROM superheroes
    RIGHT JOIN teams ON teams.team_id = superheroes.team_id
    GROUP BY teams.team_id
)
SELECT AVG(hero_count) as average_hero_count FROM superhero_team_sizes
```

## Window Functions
- A window function performs a calculation accross a set of table rows that are somehow related to the current row
- similar to aggregate functions
- but they don't squash the rows, they remain intact
- using an empty `OVER` statement let's you do a calculation without forcing you to group by
```sql
SELECT alias, team_id, SUM(movie_appearances) OVER (

)
```