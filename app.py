from flask import Flask, render_template
import csv

app = Flask(__name__)

def get_trips():
    # reading the data 
    with open('trips.csv', 'r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        # create empty list
        trips = []
        for row in reader:
            row_data = {'name': row['name'], 'start_date': row['start_date'], 'length': row['length'], 'location': row['location'], 'cost': row['cost'], 'level': row['level'], 'leader': row['leader'], 'description': row['description']}
            # appending dictionaries to list 
            trips.append(row_data)
    # returning the list of dictionaries
    return trips

def get_members():
    # reading the data
    with open('members.csv', 'r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        # create empty list
        members = []
        for row in reader:
            row_data = {'name': row['name'], 'address': row['address'], 'email': row['email'], 'date_of_birth': row['date_of_birth'], 'phone': row['phone']}
            # appending dictionaries to list
            members.append(row_data)
    # returning list of dictionaries 
    return members

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/members/')
@app.route('/members/<member_id>')
def members():
    members = get_members()
    return render_template('members.html', members=members)

@app.route('/trips/')
@app.route('/trip/<trip_id>')
def trips(trip_id=None):
    trips = get_trips()
    if trip_id:
        return render_template('trip.html', trip=trips[int(trip_id)])
    else:
        return render_template('trips.html', trips=trips)
