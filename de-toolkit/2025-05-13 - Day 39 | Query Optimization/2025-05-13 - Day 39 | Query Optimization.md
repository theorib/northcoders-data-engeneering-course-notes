# 2025-05-13 - Day 39 | Query Optimization
## B-Tree - Type of Indexing
- Nodes: data and connections are stored
    - order: n + 1 (n = num of data items it can hold)

## INDEX
```sql
CREATE INDEX index_arbitrary_name ON table_name(column_name);
```
```sql
DROP INDEX IF EXISTS index_arbitrary_name;
```

## EXPLAIN ANALYZE
- before the query will gives us information about a
```sql
EXPLAIN ANALYSE SELECT * FROM customers WHERE fist_name = 'John';
```

## Subquery Types
- Scalar
- Multi-row
- Correlated

