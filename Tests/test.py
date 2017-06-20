__author__ = 'Ido Bichler'

from Manager.BedManager import BedManager
from Manager.LoginManager import LoginManager
from DB.SqlExecuter import SqlExecuter
from Tables.TableAvailabilities import TableAvailabilities

def test_sanity():
    availabilities_object = TableAvailabilities(bed_id='B_105_4',user_id='Yoav', date='19-06-2017')
    SqlExecuter().insert_object_to_db(availabilities_object)

if __name__ == '__main__':
    test_sanity()