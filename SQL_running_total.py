# Description
#
# Given a posts table that contains a created_at timestamp column,
# write a query that returns date (without time component), a number of posts for
# a given date and a running (cumulative) total number of posts up until a given date.
# The resulting set should be ordered chronologically by date.
#
# Desired Output
#
# The resulting set should look similar to the following:
#
# date       | count | total
# -----------+-------+-------
# 2017-01-26 |    20 |    20
# 2017-01-27 |    17 |    37
# 2017-01-28 |     7 |    44
# 2017-01-29 |     8 |    52
# ...
# date - (DATE) date
# count - (INT) number of posts for a date
# total - (INT) a running (cumulative) number of posts up until a date

query = ''
CREATE VIEW c AS
(
SELECT DATE(a.created_at) AS date,
        COUNT(1) AS count
FROM posts a
GROUP BY 1
ORDER BY 1
);

SELECT t1.date, t1.count, SUM(t2.count) :: integer AS total
FROM c t1, c t2
WHERE t2.date <= t1.date
GROUP BY 1, 2
ORDER BY 1;
''

query2 = ''
SELECT
  CREATED_AT::DATE AS DATE,
  COUNT(CREATED_AT) AS COUNT,
  SUM(COUNT(CREATED_AT)) OVER
  (ORDER BY CREATED_AT::DATE ROWS UNBOUNDED PRECEDING)::INT AS TOTAL
FROM
  POSTS
GROUP BY
  CREATED_AT::DATE
''
