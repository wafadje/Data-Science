"""

You are given a table roads with the following structure:

CREATE TABLE roads (
    km_start INTEGER NOT NULL,
    km_end INTEGER NOT NULL,
    CHECK(start <= end),
    UNIQUE(start, end)
);

Each record in this table represents a contiguous road, that goes from kilometer km_start to kilometer km_end inclusive (with km_start <= km_end and length equal to km_end − km_start).

Consider the different parts covered by the roads.

Write an SQL query that returns the total length (in kilometers) of all the parts covered by roads specified in the table roads. Note that any parts of roads that are covered by several overlapping roads should be counted only once.

For example, given:

km_start | km_end
---------+--------
       1 | 6
       3 | 4
       5 | 8
      10 | 12

your query should return: 7 kilometers

Indeed, the roads cover kilometers 1 to 8 (and kilometers 8 to 10 were not covered)
"""
