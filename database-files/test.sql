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

#-------------------------------------------------------------------





