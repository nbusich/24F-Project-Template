# use coffeeStats;
#
# # Returns number of users in each category
# SELECT COUNT(DISTINCT u.id) AS NumberofUsers, u.role
# FROM user u
# GROUP BY u.role;
#
# # Returns the user/host of queries that were denied access (Suspicious)
# SET GLOBAL general_log = 'ON';
# SET GLOBAL log_output = 'TABLE';
# SELECT user_host
# FROM mysql.general_log
# WHERE command_type = 'Connect' AND argument LIKE '%DENIED%';
#
# # Returns the firstname and lastname of the admin who made the most changes since the given date
# SELECT a.firstname, a.lastname, COUNT(c.id) AS change_count
# FROM administrator a
#     JOIN changes c on c.changerID = a.id
# WHERE c.lastChange > '2023-03-20 11:30:00'
# GROUP BY a.firstName, a.lastname
# ORDER BY change_count DESC
# LIMIT 1;
#
# #Returns queries that take longer than 0.5 seconds
# SET GLOBAL slow_query_log = 'ON';
# SET GLOBAL log_output = 'TABLE';
# SET GLOBAL long_query_time = 0.5;
# SELECT *
# FROM mysql.slow_log;
#
# # Deletes associated users
# DELETE FROM administrator WHERE id = 7;
#
# UPDATE changes
# SET description = 'Optimized the 10 slowest SQL queries'
# WHERE changerID = '8';
#
#
# SELECT
#     jobListing.title AS PositionTitle,
#     company.name AS CompanyName,
#     AVG(jobListing.payPerHour) AS AvgPayPerHour,
#     COUNT(application.id) AS TotalApplications,
#     COUNT(application.id) / jobListing.numOpenings AS AcceptanceRate
# FROM
#     jobListing
# JOIN
#     company ON jobListing.companyID = company.id
# LEFT JOIN
#     application ON jobListing.id = application.listingID
# GROUP BY
#     jobListing.id, company.name;
#
# SELECT
#     student.firstName,
#     student.lastName,
#     jobListing.title AS JobTitle,
#     jobListing.description AS JobDescription,
#     jobListing.requiredGPA,
#     student.gpa
# FROM student
# JOIN
#     jobListing ON student.gpa >= jobListing.requiredGPA
# WHERE
#     student.id = 1;
#
#
# SELECT
#     s1.firstName AS StudentFirstName,
#     s1.lastName AS StudentLastName,
#     s1.major AS Major,
#     s2.firstName AS PeerFirstName,
#     s2.lastName AS PeerLastName
# FROM
#     student AS s1
# JOIN
#     student AS s2 ON s1.major = s2.major AND s1.id != s2.id
# WHERE
#     s1.id = 1;
#
#
#
#
#
# SELECT j.acceptanceRate
# FROM jobListing j;
#
#
#
# SELECT AVG(j.requiredGPA) as AvgGPA, c.name
# FROM jobListing j
#     JOIN user u on j.companyID = u.id
#     JOIN company c on u.id = c.id
# GROUP BY companyID;
#
#
#
#
# SELECT s.firstName, s.lastName, s.id
# FROM student s
# JOIN position p ON s.pastPositionID = p.id
# JOIN user ON p.companyID = user.id
# WHERE user.id = 10;
#
#
# INSERT INTO friends (friend1ID, friend2ID) VALUES
# (1, 3);
#
#
#
# SELECT l.title, l.payPerHour, l.companyID
# FROM jobListing l
# 	JOIN relevantMajors rm ON l.id = rm.listingID
# WHERE rm.major = 'Computer Science'
# ORDER BY payPerHour DESC;
#
#
#
# INSERT INTO chatroom (receiverID, senderID) VALUES
# (3, 10);
# INSERT INTO message (chatroomID, senderID, content) VALUES
# (1, 3, 'Hi, my name is Alex. I was wondering if you could tell me what the typical dress code is like at BioHealth. Thanks!');
#
#
# SELECT m.content
# FROM message m
#         JOIN chatroom c ON m.chatroomID = c.id
#         JOIN user u ON c.senderID = u.id;
#
# SELECT
#     student.firstName,
#     student.lastName,
#     student.resume,
#     student.major,
#     application.coverLetter,
#     jobListing.title AS JobTitle,
#     jobListing.description AS JobDescription
# FROM
#     student
# JOIN
#     application ON student.id = application.applicantID
# JOIN
#     jobListing ON application.listingID = jobListing.id
# WHERE
#     student.id = 1;
#
#
#
# INSERT INTO chatroom (receiverID, senderID)
# SELECT
#     advisor.id AS AdvisorID,
#     company.id AS CompanyID
# FROM
#     application
# JOIN
#     student ON application.applicantID = student.id
# JOIN
#     advisor ON student.advisorID = advisor.id
# JOIN
#     jobListing ON application.listingID = jobListing.id
# JOIN
#     company ON jobListing.companyID = company.id
# WHERE
#     application.id = 1;
#
#
# SELECT
#     jobListing.title AS PositionTitle,
#     COUNT(application.id) AS NumApplicants
# FROM
#     jobListing
# LEFT JOIN
#     application ON jobListing.id = application.listingID
# GROUP BY
#     jobListing.id;
#
#
#
#
# SELECT c.name FROM company c
# JOIN position p ON p.companyID = c.id
#    WHERE p.companyID IN (
#        SELECT c.id FROM company c
# JOIN position p ON p.companyID = c.id
#                    JOIN student s ON s.pastPositionID = p.id
#        );
#
# SELECT m.content
# FROM message m
# JOIN chatroom c ON m.chatroomID = c.id
# JOIN user u ON c.senderID = u.id WHERE c.receiverID IN
# (
# SELECT u.id FROM user u
# JOIN student s ON u.id = s.id WHERE u.role = 'student'
# ) AND c.senderID IN (
# SELECT u.id FROM user u
# JOIN alumnus a ON u.id = a.id WHERE u.role = 'alumnus'
# );
#
# SELECT s.firstName, s.lastName
# FROM student s
# WHERE major = 'Biology';
#
# SELECT m.content
# FROM message m
# JOIN chatroom c ON m.chatroomID = c.id
# JOIN user u ON c.senderID = u.id
# JOIN student s ON u.id = s.id
# WHERE u.role ='student' AND s.major = 'Biology';
#
#
# SELECT u.email, a.firstName, a.lastName
# FROM user u
# JOIN alumnus a ON u.id = a.id
# WHERE u.role = 'alumnus';
#
#
# INSERT INTO jobListing (requiredGPA, numOpenings, applicationDeadline, payPerHour, numApplicants, description, title, companyID)
# VALUES (3.5, 2, '2025-01-27', 24.0, 0, 'Heal the world! With tech!', 'Pharmacy IT Assistant Co-op', 4);
#
#
# INSERT INTO relevantFields (listingID, field)
# VALUES (1, 'Information Technology');
#
#
# SELECT s.firstName, s.lastName, s.resume, s.id, s.advisorID
# FROM relevantMajors rm
# JOIN jobListing ON rm.listingId = jobListing.id
# JOIN student s ON rm.major = s.major;
#
#
# INSERT INTO chatroom (receiverID, senderID) VALUES
# (10, 3);
# INSERT INTO message (chatroomID, senderID, content) VALUES
# (1, 10, 'Hello Alex! I’m Janice Dean from BioHealth and I’m contacting you because you seem like potentially a great fit for our Spring 2025 Pharma Lab Co-op in the Boston area.');
#
#
# INSERT INTO chatroom (receiverID, senderID) VALUES
# (15, 10);
# INSERT INTO message (chatroomID, senderID, content) VALUES
# (1, 15, 'Hi, this is Nina, one of the Co-op Advisors at Northeastern. I’d like to inform you of our recently-added 100-application limit.');
#
#
# INSERT INTO article (title, body, publisherID)
# VALUES ('What our co-ops wish they knew going in', 'Landing a first co-op can be an exciting but stressful process…', 10);