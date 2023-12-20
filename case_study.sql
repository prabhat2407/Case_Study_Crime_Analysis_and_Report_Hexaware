create database cars;
use cars;

CREATE TABLE Victims (
    VictimID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    DateOfBirth DATE,
    Gender VARCHAR(10),
    Address VARCHAR(255),
    PhoneNumber VARCHAR(15)
);

CREATE TABLE Suspects (
    SuspectID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    DateOfBirth DATE,
    Gender VARCHAR(10),
    Address VARCHAR(255),
    PhoneNumber VARCHAR(15)
);

CREATE TABLE LawEnforcementAgencies (
    AgencyID INT PRIMARY KEY AUTO_INCREMENT,
    AgencyName VARCHAR(255),
    Jurisdiction VARCHAR(255),
    ContactInformation VARCHAR(255)
);

CREATE TABLE Officers (
    OfficerID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    BadgeNumber VARCHAR(20),
    `Rank` VARCHAR(50),
    ContactInformation VARCHAR(255),
    AgencyID INT,
    FOREIGN KEY (AgencyID) REFERENCES LawEnforcementAgencies(AgencyID)
);

CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,
    CaseDescription TEXT
);

CREATE TABLE Incidents (
    IncidentID INT PRIMARY KEY AUTO_INCREMENT,
    IncidentType VARCHAR(255),
    IncidentDate DATE,
    LocationLat DECIMAL(10, 8),
    LocationLong DECIMAL(11, 8),
    Description TEXT,
    Status VARCHAR(50),
    VictimID INT,
    SuspectID INT,
    AgencyID INT,
    CaseID INT,
    FOREIGN KEY(CaseID) REFERENCES Cases(CaseID),
    FOREIGN KEY (VictimID) REFERENCES Victims(VictimID),
    FOREIGN KEY (SuspectID) REFERENCES Suspects(SuspectID),
    FOREIGN KEY (AgencyID) REFERENCES LawEnforcementAgencies(AgencyID)
);

CREATE TABLE Evidence (
    EvidenceID INT PRIMARY KEY AUTO_INCREMENT,
    Description TEXT,
    LocationFound VARCHAR(255),
    IncidentID INT,
    FOREIGN KEY (IncidentID) REFERENCES Incidents(IncidentID)
);

CREATE TABLE Reports (
    ReportID INT PRIMARY KEY AUTO_INCREMENT,
    IncidentID INT,
    ReportingOfficerID INT,
    ReportDate DATE,
    ReportDetails TEXT,
    Status VARCHAR(50),
    FOREIGN KEY (IncidentID) REFERENCES Incidents(IncidentID),
    FOREIGN KEY (ReportingOfficerID) REFERENCES Officers(OfficerID)
);

-- Inserting 5 records into Victims table
INSERT INTO Victims (FirstName, LastName, DateOfBirth, Gender, Address, PhoneNumber)
VALUES
    ('John', 'Doe', '1990-01-15', 'Male', '123 Main St, City', '555-1234'),
    ('Jane', 'Smith', '1985-05-20', 'Female', '456 Oak St, Town', '555-5678'),
    ('Robert', 'Johnson', '1992-08-10', 'Male', '789 Elm St, Village', '555-9876'),
    ('Emily', 'Taylor', '1988-03-25', 'Female', '101 Pine St, Hamlet', '555-4321'),
    ('David', 'Clark', '1995-11-05', 'Male', '202 Cedar St, Suburb', '555-8765');

-- Inserting 5 records into Suspects table
INSERT INTO Suspects (FirstName, LastName, DateOfBirth, Gender, Address, PhoneNumber)
VALUES
    ('Michael', 'Brown', '1982-07-12', 'Male', '111 Maple St, City', '555-1111'),
    ('Sophia', 'Martinez', '1989-04-18', 'Female', '222 Birch St, Town', '555-2222'),
    ('Christopher', 'Anderson', '1994-09-03', 'Male', '333 Pine St, Village', '555-3333'),
    ('Olivia', 'Lee', '1987-12-30', 'Female', '444 Cedar St, Hamlet', '555-4444'),
    ('Matthew', 'Wang', '1998-06-08', 'Male', '555 Oak St, Suburb', '555-5555');

-- Inserting 5 records into LawEnforcementAgencies table
INSERT INTO LawEnforcementAgencies (AgencyName, Jurisdiction, ContactInformation)
VALUES
    ('City Police Department', 'City', '123 Police Plaza, City | 555-1000'),
    ('County Sheriff Office', 'County', '456 Sheriff St, County | 555-2000'),
    ('State Bureau of Investigation', 'State', '789 SBI Lane, State | 555-3000'),
    ('Federal Bureau of Investigation', 'Federal', '101 FBI Blvd, Federal | 555-4000'),
    ('Drug Enforcement Administration', 'National', '202 DEA Drive, National | 555-5000');

-- Inserting 5 records into Officers table
INSERT INTO Officers (FirstName, LastName, BadgeNumber, `Rank`, ContactInformation, AgencyID)
VALUES
    ('Officer', 'Smith', '12345', 'Detective', '123 Main St, City | 555-1234', 1),
    ('Officer', 'Johnson', '67890', 'Sergeant', '456 Oak St, Town | 555-5678', 2),
    ('Agent', 'Brown', '54321', 'Special Agent', '789 Elm St, Village | 555-9876', 4),
    ('Officer', 'Davis', '98765', 'Lieutenant', '101 Pine St, Hamlet | 555-4321', 3),
    ('Agent', 'Williams', '13579', 'Supervisory Special Agent', '202 Cedar St, Suburb | 555-8765', 5);

-- Inserting 5 records into Cases table
INSERT INTO Cases (CaseDescription)
VALUES
    ('Bank Robbery Investigation'),
    ('Assault Case'),
    ('Residential Burglary Case'),
    ('Kidnapping Case'),
    ('Homicide Investigation');
    
-- Inserting 5 records into Incidents table
INSERT INTO Incidents (IncidentType, IncidentDate, LocationLat, LocationLong, Description, Status, VictimID, SuspectID, AgencyID, CaseID)
VALUES
    ('Robbery', '2023-01-10', 40.7128, -74.0060, 'Armed robbery at the bank', 'Open', 1, 1, 1, 1),
    ('Assault', '2023-02-15', 34.0522, -118.2437, 'Physical assault in downtown', 'Closed', 2, 2, 2, 2),
    ('Burglary', '2023-03-20', 41.8781, -87.6298, 'Residential burglary in the suburbs', 'Open', 3, 3, 3, 3),
    ('Kidnapping', '2023-04-25', 33.7490, -84.3880, 'Child abduction in the city', 'Open', 4, 4, 4, 4),
    ('Homicide', '2023-05-30', 37.7749, -122.4194, 'Murder investigation in the county', 'Closed', 5, 5, 5, 5);

-- Inserting 5 records into Evidence table
INSERT INTO Evidence (Description, LocationFound, IncidentID)
VALUES
    ('Weapon found at the crime scene', 'Bank premises', 1),
    ('Security footage from the incident', 'Downtown area', 2),
    ('Burglar tools left at the scene', 'Residence', 3),
    ('Note left by kidnapper', 'City park', 4),
    ('Forensic evidence from the crime scene', 'County area', 5);

-- Inserting 5 records into Reports table
INSERT INTO Reports (IncidentID, ReportingOfficerID, ReportDate, ReportDetails, Status)
VALUES
    (1, 1, '2023-01-11', 'Investigation ongoing', 'Open'),
    (2, 2, '2023-02-16', 'Assailant apprehended', 'Closed'),
    (3, 3, '2023-03-21', 'Evidence collected, suspects at large', 'Open'),
    (4, 4, '2023-04-26', 'Search in progress for the missing child', 'Open'),
    (5, 5, '2023-05-31', 'Case closed after suspect arrest and trial', 'Closed');




