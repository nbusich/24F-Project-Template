DROP DATABASE IF EXISTS coffeeStats;

CREATE DATABASE coffeeStats;

USE coffeeStats;

DROP TABLE IF EXISTS changes, friends, user,
     administrator, student, jobListing,
     application, company, position, advisor,
     alumnus, chatroom, message, article,
     relevantMajors, relevantFields;

CREATE TABLE user
(
    id int AUTO_INCREMENT NOT NULL,
    role varchar(30) NOT NULL,
    email varchar(50) NOT NULL,
    userName varchar(50) NOT NULL,
    password varchar(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE administrator
(
    id int AUTO_INCREMENT NOT NULL,
    salary float,
    firstName varchar(50),
    lastname varchar(50),
    startDate datetime DEFAULT CURRENT_TIMESTAMP,
    endDate date,
    PRIMARY KEY (id),
    CONSTRAINT fk_admin_2
        FOREIGN KEY (id) REFERENCES user (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE changes
(
    id int AUTO_INCREMENT NOT NULL UNIQUE,
    lastChange datetime default CURRENT_TIMESTAMP,
    description varchar(300),
    changerID int,
    PRIMARY KEY (id),
    CONSTRAINT fk_change_1
        FOREIGN KEY (changerID) REFERENCES administrator(id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);



CREATE TABLE friends
(
    friend1ID int NOT NULL,
    friend2ID int NOT NULL,
    PRIMARY KEY (friend1ID, friend2ID),
    CONSTRAINT fk_friends_1
       FOREIGN KEY (friend1ID) REFERENCES user (id)
       ON UPDATE CASCADE
       ON DELETE CASCADE,
    CONSTRAINT fk_friends_2
       FOREIGN KEY (friend2ID) REFERENCES user (id)
       ON UPDATE CASCADE
       ON DELETE CASCADE
);


CREATE TABLE advisor
(
    id int AUTO_INCREMENT NOT NULL,
    firstName varchar(30),
    lastName varchar(30),
    PRIMARY KEY (id),
    CONSTRAINT fk_advisor_1
        FOREIGN KEY (id) REFERENCES user (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE student
(
    id int AUTO_INCREMENT NOT NULL,
    firstName varchar(50) NOT NULL,
    lastName  varchar(50) NOT NULL,
    bio       text,
    resume    text,
    major     varchar(50),
    minor     varchar(50),
    gpa       float,
    advisorID int,
    pastPositionID int,
    PRIMARY KEY (id),
    CONSTRAINT fk_student_1
        FOREIGN KEY (id) REFERENCES user (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_student_2
        FOREIGN KEY (advisorID) REFERENCES advisor (id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);


CREATE TABLE company
(
    id int AUTO_INCREMENT NOT NULL,
    name varchar(30)        NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_company_1
        FOREIGN KEY (id) REFERENCES user (id)
            ON UPDATE CASCADE
            ON DELETE CASCADE

);
CREATE TABLE alumnus
(
    id int AUTO_INCREMENT NOT NULL,
    firstName varchar (30),
    lastName varchar (30),
    jobID int,
    PRIMARY KEY (id),
    CONSTRAINT fk_alum_1
        FOREIGN KEY (id) REFERENCES user (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE chatroom
(
    id int AUTO_INCREMENT NOT NULL,
    receiverID int NOT NULL,
    senderID int NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_chat_1
        FOREIGN KEY (receiverID) REFERENCES user (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_chat_2
        FOREIGN KEY (senderID) REFERENCES user (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE

);

CREATE TABLE message
(
    id int AUTO_INCREMENT NOT NULL,
    chatroomID int,
    senderID int,
    content varchar (1500),
    PRIMARY KEY (id),
    CONSTRAINT fk_message_1
        FOREIGN KEY (chatroomID) REFERENCES chatroom (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_message_2
        FOREIGN KEY (senderID) REFERENCES user (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE position
(
    id int AUTO_INCREMENT NOT NULL,
    comment text,
    companyID int,
    PRIMARY KEY (id),
    CONSTRAINT fk_pos_1
        FOREIGN KEY (companyID) REFERENCES user (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE jobListing
(
    id                  int  AUTO_INCREMENT NOT NULL,
    requiredGPA         float,
    numOpenings         int,
    applicationDeadline date,
    payPerHour          float,
    numApplicants       int,
    description         text,
    title               varchar(75),
    acceptanceRate      float,
    companyID           int NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_jb_1
        FOREIGN KEY (companyID) REFERENCES user (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE application
(
    id int AUTO_INCREMENT NOT NULL,
    applicantID int,
    listingID  int,
    coverLetter text,
    PRIMARY KEY (id),
    CONSTRAINT fk_app_1
        FOREIGN KEY (applicantID) REFERENCES user (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_app_2
        FOREIGN KEY (listingID) REFERENCES jobListing (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE article
(
     id int AUTO_INCREMENT NOT NULL,
     title varchar(100),
     body text,
     date datetime,
     publisherID int,
     PRIMARY KEY(id, publisherID),
     CONSTRAINT fk_company
         FOREIGN KEY (publisherID) REFERENCES user (id)
         ON UPDATE CASCADE
         ON DELETE CASCADE
);

CREATE TABLE relevantMajors
(
    listingID int,
    major varchar(100),
    PRIMARY KEY(listingId, major),
    CONSTRAINT fk_rm
        FOREIGN KEY (listingID) REFERENCES jobListing (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE relevantFields
(
    listingID int,
    field varchar(200),
    PRIMARY KEY(listingId, field),
    CONSTRAINT fk_rf
        FOREIGN KEY (listingID) REFERENCES jobListing (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Populate the user table with at least four entries per role
INSERT INTO user (role, email, userName, password) VALUES
('student', 'student1@example.com', 'student1', 'pass1'),
('student', 'student2@example.com', 'student2', 'pass2'),
('student', 'student3@example.com', 'student3', 'pass3'),
('student', 'student4@example.com', 'student4', 'pass4'),
('administrator', 'admin@example.com', 'admin', 'adminpass'),
('administrator', 'admin2@example.com', 'admin2', 'adminpass2'),
('administrator', 'admin3@example.com', 'admin3', 'adminpass3'),
('administrator', 'admin4@example.com', 'admin4', 'adminpass4'),
('company', 'company@example.com', 'company1', 'compass'),
('company', 'company2@example.com', 'company2', 'compass2'),
('company', 'company3@example.com', 'company3', 'compass3'),
('company', 'company4@example.com', 'company4', 'compass4'),
('advisor', 'advisor@example.com', 'advisor1', 'advisorpass'),
('advisor', 'advisor2@example.com', 'advisor2', 'advisorpass2'),
('advisor', 'advisor3@example.com', 'advisor3', 'advisorpass3'),
('advisor', 'advisor4@example.com', 'advisor4', 'advisorpass4'),
('alumnus', 'alumnus@example.com', 'alumnus1', 'alumpass'),
('alumnus', 'alumnus2@example.com', 'alumnus2', 'alumpass2'),
('alumnus', 'alumnus3@example.com', 'alumnus3', 'alumpass3'),
('alumnus', 'alumnus4@example.com', 'alumnus4', 'alumpass4'), 
('company', 'jbaker@example.com', 'bhlarma', 'compass5');

-- Populate the administrator table
INSERT INTO administrator (id, salary, firstName, lastName, startDate) VALUES
(5, 75000, 'Alice', 'Admin', '2022-01-01'),
(6, 70000, 'Bob', 'Smith', '2022-02-01'),
(7, 72000, 'Carol', 'Johnson', '2022-03-01'),
(8, 68000, 'David', 'Williams', '2022-04-01');

-- Populate the advisor table
INSERT INTO advisor (id, firstName, lastName) VALUES
(13, 'Melissa', 'Johnson'),
(14, 'Cameron', 'Lester'),
(15, 'Nina', 'Brown'),
(16, 'Oliver', 'Davis');

-- Populate the student table
INSERT INTO student (id, firstName, lastName, bio, resume, major, minor, gpa, advisorID) VALUES
(1, 'John', 'Doe', 'Bio of John', 'Resume of John', 'Computer Science', 'Math', 3.5, 13),
(2, 'Jane', 'Smith', 'Bio of Jane', 'Resume of Jane', 'Engineering', NULL, 3.8, 13),
(3, 'Alex', 'Green', 'Bio of Alex', 'Resume of Alex', 'Biology', 'Chemistry', 3.2, 14),
(4, 'Emily', 'White', 'Bio of Emily', 'Resume of Emily', 'Mathematics', 'Physics', 3.9, 15);

-- Populate the company table
INSERT INTO company (id, name) VALUES
(9, 'TechCorp'),
(10, 'BioHealth Inc.'),
(11, 'FinServe LLC'),
(12, 'EduLearn Co.'),
(21, 'Bhlarma Advance');

-- Populate the position table
INSERT INTO position (comment, companyID) VALUES
('Software Engineer Position', 9),
('Marketing Manager Position', 10),
('Data Analyst Position', 11),
('Curriculum Developer Position', 12);

-- Populate the jobListing table
INSERT INTO jobListing (requiredGPA, numOpenings, applicationDeadline, payPerHour, numApplicants, description, title, companyID) VALUES
(3.0, 5, '2023-12-31', 30.0, 0, 'Internship opportunity at TechCorp', 'Software Engineer Intern', 9),
(3.5, 3, '2023-11-30', 28.0, 0, 'Research Assistant in Biology', 'Biology Research Intern', 10),
(3.2, 2, '2023-10-31', 25.0, 0, 'Finance internship', 'Financial Analyst Intern', 11),
(3.0, 4, '2023-12-15', 20.0, 0, 'Education sector opportunity', 'Teaching Assistant Intern', 12);

-- Populate the application table
INSERT INTO application (applicantID, listingID, coverLetter) VALUES
(1, 1, 'Cover letter from John Doe for listing 1'),
(2, 2, 'Cover letter from Jane Smith for listing 2'),
(3, 3, 'Cover letter from Alex Green for listing 3'),
(4, 4, 'Cover letter from Emily White for listing 4');

-- Populate the alumnus table
INSERT INTO alumnus (id, firstName, lastName, jobID) VALUES
(17, 'Mike', 'Alumni', 1),
(18, 'Sarah', 'Alumni', 2),
(19, 'Tom', 'Alumni', 3),
(20, 'Lisa', 'Alumni', 4);

-- Populate the friends table
INSERT INTO friends (friend1ID, friend2ID) VALUES
(1, 2),
(2, 1),
(3, 4),
(4, 3);

-- Populate the chatroom table
INSERT INTO chatroom (receiverID, senderID) VALUES
(1, 3),
(2, 4),
(3, 2),
(4, 1);

-- Populate the message table
INSERT INTO message (chatroomID, senderID, content) VALUES
(1, 3, 'Hi, John!'),
(2, 4, 'Hello, Jane!'),
(3, 2, 'Hey Alex, how are you?'),
(4, 1, 'Hi Emily, doing great!');

-- Populate the changes table
INSERT INTO changes (lastChange, description, changerID) VALUES
('2023-01-10 09:00:00', 'Updated feature settings', 5),
('2023-02-15 10:00:00', 'Fixed bug in system', 6),
('2023-03-20 11:30:00', 'Updated user interface', 7),
('2023-04-05 15:45:00', 'Database maintenance', 8);

-- Populate the article table
INSERT INTO article (title, body, date, publisherID) VALUES
('TechCorp Announces New Product', 'Details about the new product...', '2023-05-01 12:00:00', 9),
('BioHealth Inc. Research Findings', 'Latest findings in biohealth...', '2023-06-10 14:00:00', 10),
('FinServe LLC Financial Tips', 'Top 10 financial tips...', '2023-07-15 09:30:00', 11),
('EduLearn Co. Launches New Courses', 'Introducing new online courses...', '2023-08-20 16:20:00', 12);

-- Populate the relevantMajors table
INSERT INTO relevantMajors (listingID, major) VALUES
(1, 'Computer Science'),
(2, 'Biology'),
(3, 'Finance'),
(4, 'Education');

-- Populate the relevantFields table
INSERT INTO relevantFields (listingID, field) VALUES
(1, 'Software Engineering'),
(2, 'Biology Research'),
(3, 'Financial Services'),
(4, 'Teaching');


# Returns number of users in each category
SELECT COUNT(DISTINCT u.id) AS NumberofUsers, u.role
FROM user u
GROUP BY u.role;

# Returns the user/host of queries that were denied access (Suspicious)
SET GLOBAL general_log = 'ON';
SET GLOBAL log_output = 'TABLE';
SELECT user_host
FROM mysql.general_log
WHERE command_type = 'Connect' AND argument LIKE '%DENIED%';

# Returns the firstname and lastname of the admin who made the most changes since the given date
SELECT a.firstname, a.lastname, COUNT(c.id) AS change_count
FROM administrator a
    JOIN changes c on c.changerID = a.id
WHERE c.lastChange > '2023-03-20 11:30:00'
GROUP BY a.firstName, a.lastname
ORDER BY change_count DESC
LIMIT 1;

#Returns queries that take longer than 0.5 seconds
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL log_output = 'TABLE';
SET GLOBAL long_query_time = 0.5;
SELECT *
FROM mysql.slow_log;

# Deletes associated users
DELETE FROM administrator WHERE id = 7;

UPDATE changes
SET description = 'Optimized the 10 slowest SQL queries'
WHERE changerID = '8';


SELECT
    jobListing.title AS PositionTitle,
    company.name AS CompanyName,
    AVG(jobListing.payPerHour) AS AvgPayPerHour,
    COUNT(application.id) AS TotalApplications,
    COUNT(application.id) / jobListing.numOpenings AS AcceptanceRate
FROM
    jobListing
JOIN
    company ON jobListing.companyID = company.id
LEFT JOIN
    application ON jobListing.id = application.listingID
GROUP BY
    jobListing.id, company.name;

SELECT
    student.firstName,
    student.lastName,
    jobListing.title AS JobTitle,
    jobListing.description AS JobDescription,
    jobListing.requiredGPA,
    student.gpa
FROM student
JOIN
    jobListing ON student.gpa >= jobListing.requiredGPA
WHERE
    student.id = 1;


SELECT
    s1.firstName AS StudentFirstName,
    s1.lastName AS StudentLastName,
    s1.major AS Major,
    s2.firstName AS PeerFirstName,
    s2.lastName AS PeerLastName
FROM
    student AS s1
JOIN
    student AS s2 ON s1.major = s2.major AND s1.id != s2.id
WHERE
    s1.id = 1;





SELECT j.acceptanceRate
FROM jobListing j;



SELECT AVG(j.requiredGPA) as AvgGPA, c.name
FROM jobListing j
    JOIN user u on j.companyID = u.id
    JOIN company c on u.id = c.id
GROUP BY companyID;




SELECT s.firstName, s.lastName, s.id
FROM student s
JOIN position p ON s.pastPositionID = p.id
JOIN user ON p.companyID = user.id
WHERE user.id = 10;


INSERT INTO friends (friend1ID, friend2ID) VALUES
(1, 3);



SELECT l.title, l.payPerHour, l.companyID
FROM jobListing l
	JOIN relevantMajors rm ON l.id = rm.listingID
WHERE rm.major = 'Computer Science'
ORDER BY payPerHour DESC;



INSERT INTO chatroom (receiverID, senderID) VALUES
(3, 10);
INSERT INTO message (chatroomID, senderID, content) VALUES
(1, 3, 'Hi, my name is Alex. I was wondering if you could tell me what the typical dress code is like at BioHealth. Thanks!');


SELECT m.content
FROM message m
        JOIN chatroom c ON m.chatroomID = c.id
        JOIN user u ON c.senderID = u.id;

SELECT
    student.firstName,
    student.lastName,
    student.resume,
    student.major,
    application.coverLetter,
    jobListing.title AS JobTitle,
    jobListing.description AS JobDescription
FROM
    student
JOIN
    application ON student.id = application.applicantID
JOIN
    jobListing ON application.listingID = jobListing.id
WHERE
    student.id = 1;



INSERT INTO chatroom (receiverID, senderID)
SELECT
    advisor.id AS AdvisorID,
    company.id AS CompanyID
FROM
    application
JOIN
    student ON application.applicantID = student.id
JOIN
    advisor ON student.advisorID = advisor.id
JOIN
    jobListing ON application.listingID = jobListing.id
JOIN
    company ON jobListing.companyID = company.id
WHERE
    application.id = 1;


SELECT
    jobListing.title AS PositionTitle,
    COUNT(application.id) AS NumApplicants
FROM
    jobListing
LEFT JOIN
    application ON jobListing.id = application.listingID
GROUP BY
    jobListing.id;




SELECT c.name FROM company c
JOIN position p ON p.companyID = c.id
   WHERE p.companyID IN (
       SELECT c.id FROM company c
JOIN position p ON p.companyID = c.id
                   JOIN student s ON s.pastPositionID = p.id
       );

SELECT m.content
FROM message m
JOIN chatroom c ON m.chatroomID = c.id
JOIN user u ON c.senderID = u.id WHERE c.receiverID IN
(
SELECT u.id FROM user u
JOIN student s ON u.id = s.id WHERE u.role = 'student'
) AND c.senderID IN (
SELECT u.id FROM user u
JOIN alumnus a ON u.id = a.id WHERE u.role = 'alumnus'
);

SELECT s.firstName, s.lastName
FROM student s
WHERE major = 'Biology';

SELECT m.content
FROM message m
JOIN chatroom c ON m.chatroomID = c.id
JOIN user u ON c.senderID = u.id
JOIN student s ON u.id = s.id
WHERE u.role ='student' AND s.major = 'Biology';


SELECT u.email, a.firstName, a.lastName
FROM user u
JOIN alumnus a ON u.id = a.id
WHERE u.role = 'alumnus';


INSERT INTO jobListing (requiredGPA, numOpenings, applicationDeadline, payPerHour, numApplicants, description, title, companyID)
VALUES (3.5, 2, '2025-01-27', 24.0, 0, 'Heal the world! With tech!', 'Pharmacy IT Assistant Co-op', 4);


INSERT INTO relevantFields (listingID, field)
VALUES (1, 'Information Technology');


SELECT s.firstName, s.lastName, s.resume, s.id, s.advisorID
FROM relevantMajors rm
JOIN jobListing ON rm.listingId = jobListing.id
JOIN student s ON rm.major = s.major;


INSERT INTO chatroom (receiverID, senderID) VALUES
(10, 3);
INSERT INTO message (chatroomID, senderID, content) VALUES
(1, 10, 'Hello Alex! I’m Janice Dean from BioHealth and I’m contacting you because you seem like potentially a great fit for our Spring 2025 Pharma Lab Co-op in the Boston area.');


INSERT INTO chatroom (receiverID, senderID) VALUES
(15, 10);
INSERT INTO message (chatroomID, senderID, content) VALUES
(1, 15, 'Hi, this is Nina, one of the Co-op Advisors at Northeastern. I’d like to inform you of our recently-added 100-application limit.');


INSERT INTO article (title, body, publisherID)
VALUES ('What our co-ops wish they knew going in', 'Landing a first co-op can be an exciting but stressful process…', 10);


