DROP DATABASE IF EXISTS coffeeStats;

CREATE DATABASE coffeeStats;

USE coffeeStats;

DROP TABLE IF EXISTS changes, friends, user,
     administrator, student, jobListing,
     application, company, position, advisor,
     alumnus, chatroom, message;

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
        ON DELETE RESTRICT
);

CREATE TABLE changes
(
    id int AUTO_INCREMENT NOT NULL UNIQUE,
    lastChange datetime default CURRENT_TIMESTAMP,
    description varchar(300),
    changerID int NOT NULL,
    changedID int NOT NULL,
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
    firstName varchar(30),
    lastName varchar(30),
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
    chatroomID int,
    senderID int,
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
    companyID int,
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
        ON DELETE RESTRICT
);


INSERT INTO user (role, email, userName, password) VALUES
('student', 'student1@example.com', 'student1', 'pass1'),
('student', 'student2@example.com', 'student2', 'pass2'),
('administrator', 'admin@example.com', 'admin', 'adminpass'),
('company', 'company@example.com', 'company1', 'compass'),
('advisor', 'advisor@example.com', 'advisor1', 'advisorpass');

SELECT * FROM user;

INSERT INTO administrator (id, salary, firstName, lastName, startDate) VALUES
(3, 75000, 'Alice', 'Admin', '2022-01-01');

INSERT INTO advisor (id, firstName, lastName) VALUES
(5, 'Melissa', 'Johnson'),
(4, 'Cameron', 'Lester');

INSERT INTO student (id, firstName, lastName, bio, resume, major, minor, gpa, advisorID) VALUES
(1, 'John', 'Doe', 'Bio of John', 'Resume of John', 'Computer Science', 'Math', 3.5, 5),
(2, 'Jane', 'Smith', 'Bio of Jane', 'Resume of Jane', 'Engineering', NULL, 3.8, 5);

INSERT INTO company (id, name) VALUES
(4, 'TechCorp');

INSERT INTO position (comment, companyID) VALUES
('Software Engineer Position', 4);

INSERT INTO jobListing (requiredGPA, numOpenings, applicationDeadline, payPerHour, numApplicants, description, title, companyID) VALUES
(3.0, 5, '2023-12-31', 30.0, 0, 'Internship opportunity at TechCorp', 'Software Engineer Intern', 4);

INSERT INTO application (applicantID, listingID) VALUES
(1, 1);

INSERT INTO user (role, email, userName, password) VALUES
('alumnus', 'alumnus@example.com', 'alumnus1', 'alumpass');

INSERT INTO alumnus (id, firstName, lastName, jobID) VALUES
(6, 'Mike', 'Alumni', 1);

INSERT INTO friends (friend1ID, friend2ID) VALUES
(1, 2),
(2, 1);

INSERT INTO chatroom (receiverID, senderID) VALUES
(1, 2);

INSERT INTO message (chatroomID, senderID, content) VALUES
(1, 2, 'Hello, John!');

INSERT INTO changes (lastChange, description, changerID, changedID) VALUES
('2023-01-10 09:00:00', 'Updated feature settings', 3, 1);

SELECT s.firstName, s.lastName FROM student AS s;

SELECT a.firstName, a.lastName
FROM advisor a JOIN student AS s ON a.id = s.advisorID
WHERE s.firstName = 'Jane';
