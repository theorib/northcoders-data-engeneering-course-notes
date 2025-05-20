# 2025-05-16 - Day 42 | Data Wrangling
## Series
a one dimensional data array holding data of any type
- adding 
Properties
- values
- index
- dtype

## Data frames
a two dimensional data structure comprised of series
(table-like?)

## data from one file format to another

- programmatic manipulation of large data sets

If you mix a data type in a series it assums the type is object and will accept any object
you can pre define dtype and that would not allow that

important methods `loc`, `iloc`

convention on file naming

suffix `_s` for series `_df` for data frame

.head() first five by default but can specify num