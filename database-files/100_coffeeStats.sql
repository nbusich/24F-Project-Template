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
        ON DELETE CASCADE,
    CONSTRAINT fk_alum_2
        FOREIGN KEY (jobID) REFERENCES position (id)
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
