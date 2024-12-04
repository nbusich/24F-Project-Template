use coffeeStats;

#-------------------------------------------------------------------
# Counting articles published per month

SELECT
    YEAR(date) AS year,
    MONTH(date) AS month,
    COUNT(*) AS article_count
FROM
    article
GROUP BY
    YEAR(date), MONTH(date)
ORDER BY
    YEAR(date), MONTH(date);

#-------------------------------------------------------------------
# Counting users joined per week

SELECT
    YEAR(join_date) AS year,
    WEEK(join_date) AS week,
    COUNT(*) AS user_count
FROM
    user
GROUP BY
    YEAR(join_date), WEEK(join_date)
ORDER BY
    YEAR(join_date), WEEK(join_date);

#-------------------------------------------------------------------
# Counting jobs listed per week

SELECT
    YEAR(post_date) AS year,
    WEEK(post_date) AS week,
    COUNT(*) AS listing_count
FROM
    jobListing
GROUP BY
    YEAR(post_date), WEEK(post_date)
ORDER BY
    YEAR(post_date), WEEK(post_date);

#-------------------------------------------------------------------
# Counting messages sent per week

SELECT
    YEAR(send_datetime) AS year,
    WEEK(send_datetime) AS week,
    COUNT(*) AS message_count
FROM
    message
GROUP BY
    YEAR(send_datetime), WEEK(send_datetime)
ORDER BY
    YEAR(send_datetime), WEEK(send_datetime);

#-------------------------------------------------------------------
# Counting number of users in each role

SELECT COUNT(*), role
FROM user
GROUP BY role;


SELECT
    AVG(DATEDIFF(applicationDeadline, post_date)) AS average_days_to_fill
FROM
    jobListing
WHERE
    applicationDeadline IS NOT NULL AND post_date IS NOT NULL;


SELECT
    jl.id AS job_listing_id,
    jl.title AS job_title,
    COUNT(a.id) AS application_count
FROM
    jobListing jl
LEFT JOIN
    application a ON jl.id = a.listingID
GROUP BY
    jl.id, jl.title
ORDER BY
    application_count DESC;


#-------------------------------------------------------------------ç

SHOW VARIABLES LIKE 'performance_schema';
SELECT * FROM performance_schema.events_statements_summary_global_by_event_name

####################################################################################
SELECT
    EVENT_NAME, ROUND(SUM_TIMER_WAIT/COUNT_STAR/1000000000000, 6) AS avg_exec_time_ms
FROM
    performance_schema.events_statements_summary_global_by_event_name
WHERE
    COUNT_STAR > 0 AND EVENT_NAME LIKE 'statement/sql/%';
####################################################################################

SHOW GLOBAL STATUS LIKE 'Slow_queries';

SHOW STATUS WHERE `variable_name` = 'Threads_connected'

SHOW GLOBAL STATUS LIKE 'Uptime';

SELECT
    table_name,
    ROUND((data_length + index_length) / 1024 / 1024, 2) AS size_mb
FROM
    information_schema.TABLES
WHERE
    table_schema = 'coffeeStats'
ORDER BY
    size_mb DESC;

SELECT * FROM changes ORDER BY lastChange DESC LIMIT 10;

INSERT INTO changes (description,
                            changerID)
         VALUES ('OPTIMIZED QUERIES','16')
DELETE FROM changes WHERE id = 101;