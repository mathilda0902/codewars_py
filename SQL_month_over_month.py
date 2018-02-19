# Description
#
# Given a posts table that contains a created_at timestamp column write a query
# that returns a first date of the month, a number of posts created in a given month
# and a month-over-month growth rate.
#
# The resulting set should be ordered chronologically by date.
#
# Note:
#
# percent growth rate can be negative
# percent growth rate should be rounded to one digit after the decimal point and
# immediately followed by a percent symbol "%". See the desired output below for the reference.
# Desired Output
#
# The resulting set should look similar to the following:
#
# date       | count | percent_growth
# -----------+-------+---------------
# 2016-02-01 |   175 |           null
# 2016-03-01 |   338 |          93.1%
# 2016-04-01 |   345 |           2.1%
# 2016-05-01 |   295 |         -14.5%
# 2016-06-01 |   330 |          11.9%
# ...
# date - (DATE) a first date of the month
# count - (INT) a number of posts in a given month
# percent_growth - (TEXT) a month-over-month growth rate expressed in percents

query = ''
WITH new AS
(
  SELECT
    DATE_TRUNC('month', created_at) AS date,
    COUNT(1) AS count
  FROM posts
  GROUP BY 1
  ORDER BY 1
)
SELECT
    date::date,
    count,
    ROUND(100.0 * (count - LAG(count) OVER (ORDER BY 1)) / LAG(count) OVER (ORDER BY 1) ,1)
        || '%' as percent_growth
FROM new;

''
