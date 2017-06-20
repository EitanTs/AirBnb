__author__ = 'Ido Bichler'

from Tables.TableAvailabilities import TableAvailabilities
from DB.SqlExecuter import SqlExecuter


def test_sanity():
    availabilities_object = TableAvailabilities(bed_id='B_105_4', date='19-06-2017', user_id='Bals', renter_id=None)
    is_exist_query = availabilities_object.IS_EXIST_QUERY.format(table_name=availabilities_object.table_name,
                                                                 column_key='BedId', column_value='B_105_4')
    is_exist_query += " and date='{check_in}'".format(check_in='19-06-2017')
    if not availabilities_object.is_exist('', '', query=is_exist_query):
        SqlExecuter().insert_object_to_db(availabilities_object)


if __name__ == '__main__':
    test_sanity()