
class Table(object):

    INSERT_QUERY = 'INSERT INTO {table_name} VALUES ({params_format})'
    PARAM = '?,'

    def __init__(self, table_name):
        self.table_name = table_name

    def generate_insert_query(self):
        params_format = ''
        for i in xrange(len(self.values)):
            params_format += self.PARAM
        params_format = params_format[:-1]
        return self.INSERT_QUERY.format(table_name=self.table_name, params_format=params_format)