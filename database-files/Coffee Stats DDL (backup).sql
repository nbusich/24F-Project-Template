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
    startDate datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
    endDate date,
    PRIMARY KEY (id),
    CONSTRAINT fk_admin_2
        FOREIGN KEY (id) REFERENCES user (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE changes
(
    id int AUTO_INCREMENT NOT NULL UNIQUE,
    lastChange datetime default CURRENT_TIMESTAMP,
    description varchar(300),
    changerID int NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_admin_1
        FOREIGN KEY (changerID) REFERENCES administrator(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);



CREATE TABLE friends
(
    friend1ID int NOT NULL,
    friend2ID int NOT NULL,
    PRIMARY KEY (friend1ID, friend2ID),
    CONSTRAINT fk_friends_1
       FOREIGN KEY (friend1ID) REFERENCES user (id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT,
    CONSTRAINT fk_friends_2
       FOREIGN KEY (friend2ID) REFERENCES user (id)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


CREATE TABLE advisor
(
    id int AUTO_INCREMENT NOT NULL,
    firstName varchar(30) NOT NULL,
    lastName varchar(30) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_advisor_1
        FOREIGN KEY (id) REFERENCES user (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
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
        ON DELETE RESTRICT,
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
        ON DELETE RESTRICT
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
        ON DELETE RESTRICT,
    CONSTRAINT fk_chat_2
        FOREIGN KEY (senderID) REFERENCES user (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT

);

CREATE TABLE message
(
    id int AUTO_INCREMENT NOT NULL,
    chatroomID int NOT NULL,
    senderID int NOT NULL,
    content varchar (1500),
    PRIMARY KEY (id),
    CONSTRAINT fk_message_1
        FOREIGN KEY (chatroomID) REFERENCES chatroom (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_message_2
        FOREIGN KEY (senderID) REFERENCES user (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE position
(
    id int AUTO_INCREMENT NOT NULL,
    comment text,
    companyID int NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_pos_1
        FOREIGN KEY (companyID) REFERENCES user (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
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
        ON DELETE RESTRICT
);

CREATE TABLE application
(
    id int AUTO_INCREMENT NOT NULL,
    applicantID int NOT NULL,
    listingID  int NOT NULL,
    coverLetter text,
    PRIMARY KEY (id),
    CONSTRAINT fk_app_1
        FOREIGN KEY (applicantID) REFERENCES user (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_app_2
        FOREIGN KEY (listingID) REFERENCES jobListing (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE article
(
     id int AUTO_INCREMENT NOT NULL,
     title varchar(100) NOT NULL,
     body text,
     date datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
     publisherID int NOT NULL,
     PRIMARY KEY(id, publisherID),
     CONSTRAINT fk_company
         FOREIGN KEY (publisherID) REFERENCES user (id)
         ON UPDATE CASCADE
         ON DELETE RESTRICT
);

CREATE TABLE relevantMajors
(
    listingID int NOT NULL,
    major varchar(100) NOT NULL,
    PRIMARY KEY(listingId, major),
    CONSTRAINT fk_rm
        FOREIGN KEY (listingID) REFERENCES jobListing (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE relevantFields
(
    listingID int NOT NULL,
    field varchar(200) NOT NULL,
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
('alumnus', 'alumnus4@example.com', 'alumnus4', 'alumpass4');

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
(12, 'EduLearn Co.');

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
