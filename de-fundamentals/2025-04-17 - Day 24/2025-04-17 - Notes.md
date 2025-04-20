# 2025-04-17 - Notes
## OLTP Database (online transaction processing database)
- optimized for writes
- designed to be updated frequently
- minimal redundant data
- mantains referential integrity
- normalised!


## OLAP - Online Analytics Processing
    DATA engineering is very much about converting data from OLTP to OLAP

## Data Normalization
- An effort to design our database to be optimally processed 

### Normal Forms
    A Set of guidelines we use to make our data "normalised" and ensure the high standards

#### 1NF
1. Each column only contains atomic values (single values, no list, dictionaries or any other complex data types)
2. No repeating groups (such as category1, category2, category3, etc)

#### 2NF
1. Data must be in 1NF
2. All non-key columns must rely on the full primary key
    - You should not be able to change a column that doesn't redefine the primary key?
    - 

#### 3NF
1. Data must be in 2NF
2. No transitive dependencies (non-key columns cannot depend on other non-key columns)
    example contact details depending on the company name if this is a product table

#### UNNEST
```sql
SELECT snack_name, UNNEST(categories) AS category
FROM snacks
```

All columns must match for this to work
```sql
INSERT INTO snacks_only_basic_info
    SELECT snack_name, UNNEST(categories) AS category
    FROM snacks
```

## Database Seeding
### .env
`python-dotenv`

```python
import os
from dotenv import load_dotenv
from pg8000.native import Connection
load_dotenv()

username = os.environ["PG_USERNAME"]
password = os.environ["PG_PASSWORD"]
database = os.environ["PG_DATABASE"]

def create_connection():
    connection = Connection(
        username,
        database= database,
        password=password
    )
    return connection

def close_connection(connection):
    connection.close(connection)
```