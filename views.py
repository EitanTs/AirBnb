"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Flask, request, session
from Tables.TableUsers import TableUsers
from Tables.TableRooms import TableRooms
from Tables.TableRoomRating import TableRoomRating
from Tables.TableBeds import TableBeds
from Tables.TableAvailabilities import TableAvailabilities
from DB.SqlExecuter import SqlExecuter
import Configuration

app = Flask(__name__)
app.secret_key = '123'

@app.route('/sign_in')
def sign_in():
    return render_template('SignInForm.html')


@app.route('/sign_up_first_step', methods=['POST'])
def first_sign_in_step():
    form = request.form
    session['user_id'] = form.get('user_id')
    table_user = TableUsers(**form)
    SqlExecuter().insert_object_to_db(table_user)
    return render_template('SignInSecondStep.html', param_list=Configuration.REVIEW_PARAMS)


@app.route('/sign_in_owner', methods=['POST'])
def second_sign_in_step():
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

    for param in Configuration.REVIEW_PARAMS:
        rateing_object = TableRoomRating(room_id=room_id, param_key=param, param_value=form.get(param), user_id=session['user_id'])
        SqlExecuter().insert_object_to_db(rateing_object)

    return render_template('gallery.html')


def generate_bed_id(building, room_number, bed_number):
    return Configuration.BED_ID_FORMAT.format(building=building, room_number=room_number, bed_number=bed_number)


def generate_room_id(building, room_number):
    return Configuration.ROOM_ID_FORMAT.format(building=building, room_number=room_number)
