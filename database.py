import pymysql
from app import app 

# def get_connection():
#     return pymysql.connect(host="db.luddy.indiana.edu",
#                            user="i211s23_merahn",
#                            password="my+sql=i211s23_merahn",
#                            database="i211s23_merahn",
#                            cursorclass=pymysql.cursors.DictCursor)

def get_connection():
    return pymysql.connect(host=app.config['DB_HOST'],
                           user=app.config['DB_USER'],
                           password=app.config['DB_PASS'],
                           database=app.config['DB_DATABASE'],
                           cursorclass=pymysql.cursors.DictCursor)

# WORKING
# return a list of dictionaries representing all of the trips data 
def get_trips():
    sql = "select trip_id, name, DATE_FORMAT(start_date, '%c/%e/%Y') as start_date, length, location, cost, level, leader, description from trips order by STR_TO_DATE(start_date, '%Y-%c-%d')"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

# WORKING
# takes a trip_id, returns a single dictionary containing the data for the trip with that id
def get_trip(trip_id):
    sql = "select trip_id, name, DATE_FORMAT(start_date, '%%c/%%e/%%Y') as start_date, length, location, cost, level, leader, description from trips where trip_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (trip_id))
            return cursor.fetchone()

# WORKING
# takes as input all of the data for a trip. Inserts a new trip into the trip table 
def add_trip(name, start_date, length, location, cost, level, leader, description):
    sql = "insert into trips (name, start_date, length, location, cost, level, leader, description) values (%s, %s, %s, %s, %s, %s, %s, %s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (name, start_date, length, location, cost, level, leader, description))
        conn.commit()

# WORKING
# takes a trip_id and data for a trip. Updates the trip table with new data for the trip with trip_id as it's primary key
def update_trip(trip_id, name, start_date, length, location, cost, level, leader, description): 
    sql = "update trips set name=%s, start_date=%s, length=%s, location=%s, cost=%s, level=%s, leader=%s, description=%s where trip_id=%s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (name, start_date, length, location, cost, level, leader, description, trip_id))
        conn.commit()

# WORKING
# Takes as input all of the data for a member and adds a new member to the member table
def add_member(fname, lname, address, email, dob, phone):
    sql = "insert into members (fname, lname, address, email, dob, phone) values (%s, %s, %s, %s, %s, %s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (fname, lname, address, email, dob, phone))
        conn.commit()

# WORKING 
# returns a list of dictionaries representing all of the member data   
def get_members():
    sql = "select member_id, fname, lname, address, email, DATE_FORMAT(dob, '%c/%e/%Y') as dob, phone from members order by STR_TO_DATE(dob, '%Y-%c-%d')"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

# WORKING 
# Given an member__id and member info, updates the data for the member with the given member_id in the member table
def edit_member(member_id, fname, lname, address, email, dob, phone): 
    sql = "update members set fname=%s, lname=%s, address=%s, email=%s, dob=%s, phone=%s where member_id=%s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (fname, lname, address, email, dob, phone, member_id))
        conn.commit()

# WORKING
# Takes a member_id and deletes the member with that member_id from the member table
def delete_member(member_id): 
    sql = "delete from members where member_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (member_id))
            return cursor.fetchall()
        
# WORKING
def delete_trip(trip_id): 
    sql = "delete from trips where trip_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (trip_id))
            return cursor.fetchall()
        
# WORKING 
# Takes as input a trip_id and a member_id and inserts the appropriate data into the database that indicates the member with member_id as a primary key is attending the trip with the trip_id as a primary key
def add_member_trip(trip_id, member_id): 
    sql = "insert into member_trip (trip_id, member_id) values (%s, %s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,(trip_id, member_id))
            return cursor.fetchone()

# WORKING
# Takes as input a trip_id and a member_id and deletes the data in the database that indicates that the member with member_id as a primary key is attending the trip with trip_id as a primary key.
def remove_member_trip(trip_id, member_id): 
    sql = "delete from member_trip where (trip_id, member_id) = (%s, %s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (trip_id, member_id))
            return cursor.fetchone()

# WORKING  
# Takes a trip_id and returns a list of dictionaries representing all of the members attending the trip with trip_id as its primary key
def get_attendees(trip_id): # need to test
    sql = "select * from members join member_trip on members.member_id = member_trip.member_id where member_trip.trip_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (trip_id))
            return cursor.fetchall()

# main  
if __name__ == '__main__':
    #add more test code here to make sure all your functions are working correctly
    try:
        # testing for adding trips, printing trips, and getting single trips
        add_trip("A Day in Yellowwood", "2023-04-22", '1 day', "Yellowwood State Forest", '$10', "beginner", "Sy Hikist", "A day of hiking in Yellowwood")
        print(f'All trips: {get_trips()}\n')
        print(f'Trip info for trip_id 1: {get_trip(1)}\n')

        # testing for update trip
        update_trip(4, 'Everest Base Camp Trek', '2024-01-01', '6 days', 'Everest Base Camp (Nepal)', '$3500', 'Advanced', 'Tenzing Sherpa', 'A long quest to Everest')
        print(f'Updated trip info: {get_trip(4)}\n')

        # testing for adding member, deleting member, and getting members
        add_member("Tom", "Sawyer","101 E Sam Clemons Dr Bloomington, IN","tsawyer@twain.com","1970-04-01", "(812)905-1865")
        print(f'All Members: {get_members()}\n')
        delete_member(8)
        print(f'All Members after deleting: {get_members()}\n')

        # testing for edit member
        edit_member(1, 'Michael', 'Thompson', '123 Main St', 'michael.thompson@example.com', '1987-10-05', '(123)456-7890')
        print(f'Edit member: {get_members()}\n')

        # testing for adding, removing, and printing member trips
        add_member_trip(1, 4)
        add_member_trip(1, 6)
        print(f"All members attending the trip with trip_id 1: {get_attendees(1)}\n")
        remove_member_trip(1, 4)
        print(f"All members attending the trip with trip_id 1 after removing: {get_attendees(1)}")

        # delete_trip(8)
        # print(f'All trips: {get_trips()}\n')

    except Exception as e:
        print(e)