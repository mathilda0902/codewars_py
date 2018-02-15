# Your task is to create a SQL query which returns the maximum number of
# simultaneous uses of a service. Each usage ("visit") is logged with its entry
# and exit timestamps in a "visits" table structured as follows:
#
# id          primary key
# entry_time  timestamp of visit start
# exit_time   timestamp of visit end
# A visit starts at entry time and ends at exit time. At exactly end time the visit is considered to have already finished. The visits table always contains at least one entry. Your query should return a single row, containing the following columns:
#
# when_happened  earliest timestamp when there were so many concurrent visits
# visits_count   maximum count of overlapping visits

query = '''
SELECT MIN(time) AS when_happened, MAX(overlap) AS visits_count
FROM
    (SELECT id, entry_time as time
    FROM
        visits
    WHERE
        exit_time = entry_time
    GROUP BY id) AS t1,

    (SELECT
        id as id,
        COUNT(1) AS overlap
    FROM
        visits
    WHERE
        exit_time = entry_time
    GROUP BY id) AS t2;
'''
