
"""
n research, authors get scored depending on their number of publications, and number of citations associated to their papers.

One of the most famous and watched score metric is called H-Index.

It is defined as such:

    The H-index of an author is the largest number H such that the author has written at least H publications, each of which has been cited at least H times.

You are given two tables, author and publication, with the following structure:

CREATE TABLE author (
    id integer NOT NULL,
    name VARCHAR(50) NOT NULL,
    UNIQUE(id)
);

CREATE TABLE publication (
    author_id INTEGER NOT NULL,
    title VARCHAR(100) NOT NULL,
    citations INTEGER NOT NULL,
    UNIQUE(author_id, title)
);

Each row in author table contains information about an author, who might have written some publications.

Each record in publication table represents a publication written by one of the authors from the table author. The publication has an associated number of citations.

Write a SQL query that returns a table comprising all the authors (author_id and author_name) appearing in the table author and their respective H-indices (h_index).

The table should be ordered by h_index in descending order, author_id in descending order.

For example, for:

    author:

 id | name
----+--------
  4 | Yann Le Cun
 68 | Yoshua Bengio
 49 | Andrew Y. Ng
  1 | Geoffrey Hinton
 26 | Andrej Karpathy

    publication:

author_id |         title         | cited
----------+-----------------------+-------
        1 | Boltzmann machines    |    90
        1 | Layer Normalization   |     8
        1 | Matrix Capsules       |     5
        1 | Back Propagation      |     3
        1 | The Helmholtz Machine |     0
        1 | Dropout               |     1
       26 | DenseCap              |     1

Your query should return:

author_id | author_name     | h_index
----------+-----------------+---------
        1 | Geoffrey Hinton |       3
       26 | Andrej Karpathy |       1
        4 | Yann Le Cun     |       0
       68 | Yoshua Bengio   |       0
       49 | Andrew Y. Ng    |       0

In this example, Geoffrey Hinton published at least three publications that have been cited three times or more (in fact, there are four such titles). On the other hand, no four titles have been cited four times or more, so Geoffrey's H-index has to be lower than 4. Therefore, Geoffrey's H-index is 3.

The author Andrej Karpathy has published one title (DenseCap) that has been cited once, so Andrej's H-index is 1.

The remaining authors have not published anything, so their H-indices are all 0.
"""
