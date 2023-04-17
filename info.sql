DROP TABLE IF EXISTS member_trip;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS trips;

-- creating member table
CREATE TABLE members
(
member_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
fname VARCHAR(15),
lname VARCHAR(15),
address VARCHAR(100),
email VARCHAR(50),
dob DATE,
phone VARCHAR(15)
) ENGINE=INNODB;

-- creating trip table
CREATE TABLE trips
(
trip_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50),
start_date DATE,
length VARCHAR(20),
location VARCHAR(50),
cost VARCHAR(25),
level VARCHAR(20), 
leader VARCHAR(25),
description VARCHAR(200)
) ENGINE=INNODB;

-- creating relationship table
CREATE TABLE member_trip 
(
member_id INT NOT NULL,
trip_id INT NOT NULL,
FOREIGN KEY (member_id) REFERENCES members(member_id),
FOREIGN KEY (trip_id) REFERENCES trips(trip_id)
) ENGINE=INNODB;

-- inserting values into members
INSERT INTO members (fname, lname, address, email, dob, phone) VALUES
('Michael', 'Thompson', '123 Main St', 'micheal.thompson@example.com', '1968-10-05', '(123)456-7890'),
('James', 'Hernandez', '789 Oak St', 'james.hernandez@example.com', '1989-10-11', '(260)555-1234'),
('Emily', 'Davis', '901 Oakwood Ave', 'emily.davis@example.com', '1990-12-08', '(812)555-9876'),
('Sarah', 'Nguyen', '456 Elm St', 'sarah.nguyen@example.com', '1992-12-06', '(098)765-4321'),
('Samantha', 'Patel', '321 Maple St', 'samantha.patel@example.com', '1994-03-02', '(555)123-4567'),
('Daniel', 'Kim', '567 Pine St', 'daniel.kim@example.com', '1997-01-06','(812)987-6543'),
('Jane', 'Doe', '123 Example Ln', 'jane.doe@example.com', '1976-08-29', '(555)555-5555');

--inserting values into trips
INSERT INTO trips (name, start_date, length, location, cost, level, leader, description) VALUES
('Machu Picchu Explorer', '2023-05-15', '4 days', 'Machu Picchu (Peru)', '$2500', 'Intermediate', 'Maria Sanchez', 'An exploritory hike to Machu Picchu'),
('Mirandas Mountain Hike', '2023-05-27', '1 day', 'Smokey Mountains (Tennessee)', '$1000', 'beginner', 'Miranda', 'A hike through the smokey mountains'),
('Rocky Mountain High Adventure', '2023-08-01', '7 days', 'Rocky Mountain National Park (Colorado)', '$3800', 'Advanced', 'John Parker', 'An adventure through the Rocky Mountains'),
('Everest Base Camp Trek', '2024-01-01', '7 days', 'Everest Base Camp (Nepal)', '$3500', 'Advanced', 'Tenzing Sherpa','A long quest to Everest'),
('Amazon Rainforest Expedition', '2024-03-15', '3 days', 'Amazon Rainforest (Brazil)', '$2000', 'Intermediate', 'Ana Silva', 'An expedition through the Amazon'),
('Canadian Wilderness Canoe Trip', '2024-07-01', '2 days', 'Algonquin Provincial Park (Canada)', '$1200', 'Beginner', 'David Thompson', 'Exploring the Canadian wilderness'),
('Patagonia Multi-Sport Adventure', '2024-11-01', '6 days', 'Torres del Paine National Park (Chile)', '$3500', 'Advanced', 'Sofia Torres', 'An adventure full of activities in Patagonia');
