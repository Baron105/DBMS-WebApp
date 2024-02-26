
CREATE table student (
    roll Varchar(9) NOT NULL,
    fest_id numeric(5) PRIMARY KEY,
    name Varchar(50) NOT NULL,
    dept Varchar(50) NOT NULL
);

CREATE table event(
    event_id numeric(5) NOT NULL PRIMARY KEY,
    event_name Varchar(50) NOT NULL,
    event_date date NOT NULL,
    event_time time NOT NULL,
    event_venue Varchar(50) NOT NULL,
    event_type Varchar(50) NOT NULL,
    event_description Varchar(100) ,
    event_winner Varchar(50)
);

CREATE table accomodation(
    acc_id numeric(5) NOT NULL PRIMARY KEY,
    name Varchar(50) NOT NULL,
    capacity INT NOT NULL
);

CREATE table ext_participant(
    fest_id numeric(5) NOT NULL PRIMARY KEY,
    name Varchar(50) NOT NULL,
    college Varchar(50) NOT NULL,
    acc_id numeric(5) NOT NULL,
    FOREIGN KEY (acc_id) REFERENCES accomodation(acc_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- relationships 
CREATE table organising(
    fest_id numeric(5) NOT NULL,
    event_id numeric(5) NOT NULL ,
    FOREIGN KEY (fest_id) REFERENCES student(fest_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (event_id) REFERENCES event(event_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    PRIMARY KEY(fest_id,event_id)
);

CREATE table volunteering(
    fest_id numeric(5) NOT NULL,
    event_id numeric(5) NOT NULL ,
    FOREIGN KEY (fest_id) REFERENCES student(fest_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (event_id) REFERENCES event(event_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    PRIMARY KEY(fest_id,event_id)
);

CREATE table participating_ext(
    fest_id numeric(5) NOT NULL,
    event_id numeric(5) NOT NULL ,
    FOREIGN KEY (fest_id) REFERENCES ext_participant(fest_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (event_id) REFERENCES event(event_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    PRIMARY KEY(fest_id,event_id)
);

CREATE table participating_int(
    fest_id numeric(5) NOT NULL,
    event_id numeric(5) NOT NULL ,
    FOREIGN KEY (fest_id) REFERENCES student(fest_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (event_id) REFERENCES event(event_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    PRIMARY KEY(fest_id,event_id)
);







