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



SELECT
    YEAR(join_date) AS year,
    MONTH(join_date) AS month,
    COUNT(*) AS user_count
FROM
    user
GROUP BY
    YEAR(join_date), MONTH(join_date)
ORDER BY
    YEAR(join_date), MONTH(join_date);
