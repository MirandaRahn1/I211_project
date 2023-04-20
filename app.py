from flask import Flask, render_template, url_for, request, redirect
# import csv
# from datetime import datetime
from os.path import exists 


app = Flask(__name__)
if exists(app.root_path + '/config.py'):
    app.config.from_pyfile(app.root_path + '/config.py')

import database

# paths :)
# MEMBERS_PATH = app.root_path + '/members.csv'
# NEW_MEMBERS_PATH= app.root_path + '/new_members.csv'
# TRIPS_PATH = app.root_path + '/trips.csv'
# NEW_TRIPS_PATH = app.root_path + '/new_trips.csv'

# def get_trips():
#     # reading the data 
#     with open(TRIPS_PATH, 'r', newline='', encoding='utf-8-sig') as csvfile:
#         reader = csv.DictReader(csvfile)
#         # create empty list
#         trips = []
#         for row in reader:
#             row_data = {'name': row['name'], 'start_date': row['start_date'], 'length': row['length'], 'location': row['location'], 'cost': row['cost'], 'level': row['level'], 'leader': row['leader'], 'description': row['description']}
#             # appending dictionaries to list 
#             trips.append(row_data)
#         # sorting trips by start date
#         sorted_trips = sorted(trips, key=lambda x: datetime.strptime(x['start_date'], '%m/%d/%Y'))
#     # returning sorted list
#     return sorted_trips

# def set_trips(trips):
    # getting the headers
    # fieldnames = list(trips[0].keys())
    # # writing data into new csv because it kept deleting my data so I wrote it into a new csv file so it wouldn't get confused
    # with open(TRIPS_PATH, 'w', newline='', encoding='utf-8-sig') as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames) #I looked up how to use DictWriter because I wasn't sure if I could just use csv.writer, and it told me I needed fieldnames
    #     writer.writeheader()
    #     for trip in trips:
    #         writer.writerow(trip)

# def get_members():
#     # reading the data
#     with open(MEMBERS_PATH, 'r', newline='', encoding='utf-8-sig') as csvfile:
#         reader = csv.DictReader(csvfile)
#         # create empty list
#         members = []
#         for row in reader:
#             row_data = {'name': row['name'], 'address': row['address'], 'email': row['email'], 'date_of_birth': row['date_of_birth'], 'phone': row['phone']}
#             # appending dictionaries to list
#             members.append(row_data)
#         # sorting members by date of birth
#         sorted_members = sorted(members, key=lambda x: datetime.strptime(x['date_of_birth'], '%m/%d/%Y'))
#     # returning sorted list
#     return sorted_members

# def set_members(members):
#     # getting the headers
#     fieldnames = list(members[0].keys())
#     # again, writing data into new csv file so it doesn't override and get confusing 
#     with open(MEMBERS_PATH, 'w', newline='', encoding='utf-8-sig') as csvfile:
#         # using fieldnames again 
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         for member in members:
#             writer.writerow(member)

# index route
@app.route('/')
def index():
    return render_template('index.html')

# members route
@app.route('/members/')
@app.route('/members/<member_id>')
def members():
    members = database.get_members()
    return render_template('members.html', members=members)

# trips route
@app.route('/trips/')
@app.route('/trip/<trip_id>')
def trips(trip_id=None):
    # trips = get_trips()
    trips = database.get_trips()

    if trip_id:
        return render_template('trip.html', trip=database.get_trip(trip_id), trip_id=trip_id)
    else:
        return render_template('trips.html', trips=trips)
    
# add members route
@app.route('/members/add/', methods = ['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        in_fname = request.form['fname']
        in_lname = request.form['lname']
        in_address = request.form['address']
        in_email = request.form['email']
        in_dob = request.form['dob']
        # getting dob to format correctly
        # in_date_of_birth = datetime.strptime(in_date_of_birth,'%Y-%m-%d')
        # in_format_date = in_date_of_birth.strftime('%m/%d/%Y')
        in_phone = request.form['phone']

        # new member disctionary
        # new_member = {'name':in_name, 'address':in_address, 'email':in_email, 'date_of_birth':in_format_date, 'phone':in_phone}
        database.add_member(in_fname, in_lname, in_address, in_email, in_dob, in_phone)
        # print(new_member)
        # members = get_members()
        # members.append(new_member)
        # set_members(members)

        return redirect(url_for('members'))
    else:
        return render_template('member_form.html')
    
# add new trip route
@app.route('/trips/create/', methods = ['GET', 'POST'])
def add_trip():
    if request.method == 'POST':
        in_name = request.form['name']
        in_start_date = request.form['start-date']
        # getting date to format correctly
        # in_start_date = datetime.strptime(in_start_date,'%Y-%m-%d')
        # in_format_date = in_start_date.strftime('%m/%d/%Y')
        in_length = request.form['length']
        in_location = request.form['location']
        in_cost = request.form['cost']
        in_level = request.form['level']
        in_leader = request.form['leader']
        in_description = request.form['description']

        # new trip dictionary
        # new_trip = {'name':in_name, 'start_date':in_format_date, 'length':in_length, 'location':in_location, 'cost':in_cost, 'level':in_level, 'leader':in_leader, 'description':in_description}
        database.add_trip(in_name, in_start_date, in_length, in_location, in_cost, in_level, in_leader, in_description)
        # trips = get_trips()
        # trips.append(new_trip)
        # set_trips(trips)

        return redirect(url_for('trips'))
    else:
        return render_template('trip_form.html')
    
# edit trip route
@app.route('/trips/<trip_id>/edit', methods = ['GET', 'POST'])
def edit_trip(trip_id=None):
    if request.method == 'POST':
        in_name = request.form['name']
        in_start_date = request.form['start-date']
        # in_start_date = datetime.strptime(in_start_date,'%Y-%m-%d')
        # in_format_date = in_start_date.strftime('%m/%d/%Y')
        in_length = request.form['length']
        in_location = request.form['location']
        in_cost = request.form['cost']
        in_level = request.form['level']
        in_leader = request.form['leader']
        in_description = request.form['description']

        # new new trip dictionary 
        # new_trip = {'name':in_name, 'start_date':in_format_date, 'length':in_length, 'location':in_location, 'cost':in_cost, 'level':in_level, 'leader':in_leader, 'description':in_description}
        database.update_trip(trip_id, in_name, in_start_date, in_length, in_location, in_cost, in_level, in_leader, in_description)
        # replaces data instead of adding 
        # trips = get_trips()
        # trips[int(trip_id)] = new_trip 
        # set_trips(trips)
        return redirect(url_for('trips', trip_id=trip_id))
        
    else:
        trip = database.get_trip(trip_id)
        # trips = get_trips()
        # trip=trips[int(trip_id)]
        # # getting the date to load in when you edit a trip
        # trip['start_date'] = datetime.strptime(trip['start_date'],'%m/%d/%Y')
        # trip['start_date'] = trip['start_date'].strftime('%Y-%m-%d')
        return render_template('trip_form.html',trip = trip )
    
# delete trip route 
@app.route('/trip/<trip_id>/delete', methods=['GET', "POST"])
def delete_trip(trip_id=None):
    trip_id = int(trip_id)
    delete=request.args.get('delete', None)
    trips=database.get_trips()
    trip=database.get_trip(trip_id)
    if delete == trip:
        del trip
        # database.get_trip(trip_id)
        return redirect(url_for('trips', trip=trips))
    else:
        return render_template('delete_form.html', trip_id=trip_id, trip=trip)