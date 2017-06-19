"""
Routes and views for the flask application.
"""

from flask import render_template, Flask, request, session, url_for
from Tables.TableUsers import TableUsers
from Tables.TableRooms import TableRooms
from Tables.TableRoomRating import TableRoomRating
from Tables.TableBeds import TableBeds
from Tables.TableAvailabilities import TableAvailabilities
from Tables.TablePreferences import TablePreferences
from Manager.BedManager import BedManager
from Manager.LoginManager import LoginManager
from DB.SqlExecuter import SqlExecuter
import Configuration

app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
@app.route('/sign_in')
def sign_in():
    return render_template('SignInForm.html')


@app.route('/sign_up_first_step', methods=['POST'])
def first_sign_in_step():
    form = request.form
    session['user_id'] = form.get('user_id')
    table_user = TableUsers(user_id=form.get('user_id'), password=form.get('password'),
                            first_name=form.get('first_name'), last_name=form.get('last_name'),
                            phone_number=form.get('phone_number'), voip=form.get('voip'), is_owner=form.get('owner'))
    SqlExecuter().insert_object_to_db(table_user)
    return render_template('SignInSecondStep.html', param_list=Configuration.REVIEW_PARAMS)


@app.route('/sign_in_owner', methods=['POST'])
def owner_sign_in():
    form = request.form
    building = form.get('building')
    room_number = form.get('room_number')
    bed_number = form.get('bed_number')
    description = form.get('description')
    bed_id = generate_bed_id(room_number=room_number, building=building,
                             bed_number=bed_number)
    room_id = generate_room_id(building=building, room_number=room_number)

    bed_object = TableBeds(bed_id=bed_id, user_id=session['user_id'], bed_number=bed_number, room_id=room_id,
                           description=description)
    room_table = TableRooms(room_id=room_id, building=building,
                            room_number=room_number)

    SqlExecuter().insert_object_to_db(bed_object)
    SqlExecuter().insert_object_to_db(room_table)

    rating_object = TableRoomRating(room_id=room_id, param_key='description', param_value=form.get('description'),
                                    user_id=session['user_id'])
    SqlExecuter().insert_object_to_db(rating_object)

    for param in Configuration.REVIEW_PARAMS:
        rating_object = TableRoomRating(room_id=room_id, param_key=param, param_value=form.get(param),
                                        user_id=session['user_id'])
        SqlExecuter().insert_object_to_db(rating_object)

    return render_template('gallery.html')


@app.route('/sign_in_renter', methods=['POST'])
def renter_sign_in():
    form = request.form
    for param in Configuration.REVIEW_PARAMS:
        rating_object = TablePreferences(param_key=param, param_value=form.get(param), user_id=session['user_id'])
        SqlExecuter().insert_object_to_db(rating_object)

    return render_template('gallery.html')


@app.route('/get_beds/<check_in>/<check_out>')
def get_beds(check_in, check_out):
    beds_objects = BedManager(session['user_id'], check_in, check_out)
    return render_template('beds.html', bed_objects=beds_objects)


@app.route('/login', methods=['POST'])
def login():
    form = request.form
    is_valid = LoginManager(form.get('user_id'), form.get('password'))
    if is_valid:
        return render_template('index.html')
    return render_template('login.html')


@app.route('/review', methods=['POST'])
def enter_bed_review():
    form = request.form
    room_id = form.get('room_id')
    current_user = session['user_id']
    rating_object = TableRoomRating(room_id=room_id, param_key='description', param_value=form.get('description'),
                                    user_id=current_user)
    SqlExecuter().insert_object_to_db(rating_object)

    for param in Configuration.REVIEW_PARAMS:
        rating_object = TableRoomRating(room_id=room_id, param_key=param, param_value=form.get(param),
                                        user_id=current_user)
        SqlExecuter().insert_object_to_db(rating_object)


def generate_bed_id(building, room_number, bed_number):
    return Configuration.BED_ID_FORMAT.format(building=building, room_number=room_number, bed_number=bed_number)


def generate_room_id(building, room_number):
    return Configuration.ROOM_ID_FORMAT.format(building=building, room_number=room_number)
