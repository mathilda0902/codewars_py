# the first 90 fibonacci numbers:
WITH RECURSIVE f (first, second) AS
(
    SELECT
        CAST(0 AS bigint),
        CAST(1 AS bigint)
    UNION ALL
    SELECT
        a.second AS first,
        a.first+a.second AS second
    FROM f as a
)
SELECT fn.first FROM f as fn
LIMIT 90;
