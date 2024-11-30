/*
CREATE DATABASE coffeeStats;

USE coffeeStats;

CREATE TABLE feature
(
    id int NOT NULL,
    creatorID int,
    userID int
);

CREATE TABLE changes
(
    id int NOT NULL,
    timestamp datetime,
    changerID int,
    changedID int
);

CREATE TABLE friends
(
    friend1ID int,
    friend2ID int
);

CREATE TABLE user
(
    id int,
    userID int,
    role varchar(30)
);


CREATE TABLE administrator
(
    id int,
    hireDate date,
    salary float,
    birthday date,
    firstname varchar(50),
    lastname varchar(50),
    startDate date,
    endDate date
);


CREATE TABLE student
(
    studentID int          NOT NULL,
    userName  varchar(30)  NOT NULL,
    firstName varchar(50)  NOT NULL,
    lastName  varchar(50)  NOT NULL,
    email     varchar(75),
    password  varchar(128) NOT NULL,
    bio       text,
    resume    text,
    major     varchar(50),
    minor     varchar(50),
    gpa       float
);


CREATE TABLE jobListing
(
    id                  int NOT NULL,
    requiredGPA         float,
    numOpenings         int,
    applicationDeadline date,
    payPerHour          float,
    numApplicants       int,
    description         text,
    title               varchar(75),
    companyID           int NOT NULL

);

CREATE TABLE application
(
    id int,
    applicantID int,
    positionID int
);

CREATE TABLE company
(
    id           int,
    name         varchar(100),
    contactEmail varchar(75)
);

CREATE TABLE position
(
    id      int,
    comment text,
    companyID int
);

CREATE TABLE advisor
(
    id        int,
    email     varchar(75),
    firstName varchar(50),
    lastName  varchar(50),
    studentID int
);

CREATE TABLE alumnus
(
    id        int,
    firstName varchar(50),
    lastName  varchar(50),
    jobID     int,
    email     varchar(75)
);

CREATE TABLE chatroom
(
    id         int,
    receiverID int,
    senderID   int
);

CREATE TABLE message
(
    id         int,
    chatroomID int,
    senderID   int
);

*/