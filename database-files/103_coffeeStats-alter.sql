USE coffeeStats;
#-------------------------------------------------------------------
# Adding datetime to user

ALTER TABLE user
ADD COLUMN join_date DATETIME DEFAULT CURRENT_TIMESTAMP;

UPDATE user
SET join_date = DATE_ADD(
    CURDATE(),
    INTERVAL -FLOOR(RAND() * 730) DAY
) + INTERVAL FLOOR(RAND() * 86400) SECOND;

#-------------------------------------------------------------------
# Adding datetime to message

ALTER TABLE message
ADD COLUMN send_datetime DATETIME  DEFAULT CURRENT_TIMESTAMP;

UPDATE message
SET send_datetime = DATE_ADD(
    CURDATE(),
    INTERVAL -FLOOR(RAND() * 730) DAY
) + INTERVAL FLOOR(RAND() * 86400) SECOND;

#-------------------------------------------------------------------
# Adding datetime to application

ALTER TABLE application
ADD COLUMN submit_date DATETIME DEFAULT CURRENT_TIMESTAMP;

UPDATE application
SET submit_date = DATE_ADD(
    CURDATE(),
    INTERVAL -FLOOR(RAND() * 89) DAY
) + INTERVAL FLOOR(RAND() * 86400) SECOND;

#-------------------------------------------------------------------
# Adding datetime to jobListing

ALTER TABLE jobListing
ADD COLUMN post_date DATETIME DEFAULT CURRENT_TIMESTAMP;

UPDATE jobListing
SET post_date = DATE_ADD(
    CURDATE(),
    INTERVAL -FLOOR(RAND() * 90) DAY
) + INTERVAL FLOOR(RAND() * 86400) SECOND;

UPDATE jobListing
SET applicationDeadline = DATE_ADD(
    CURDATE(),
    INTERVAL FLOOR(RAND() * 90) DAY
);

UPDATE jobListing
SET acceptanceRate = CASE
    WHEN RAND() < 0.75 THEN (RAND() * 0.3) + 0.001 -- 70% chance for a random value in 0-0.3
    ELSE 0.25 + (RAND() * 0.7)           -- 30% chance for a random value in 0.3-1.0
END;