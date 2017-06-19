from Tables.Table import Table


class TableUsers(Table):

    TABLE_NAME = 'Users'

    def __init__(self, user_id, password, first_name, last_name, phone_number, voip):
        super(TableUsers, self).__init__(self.TABLE_NAME)
        self.user_id = user_id[0]
        self.password = password[0]
        self.first_name = first_name[0]
        self.last_name = last_name[0]
        self.phone_number = phone_number[0]
        self.voip = voip[0]

    @property
    def values(self):
        return self.user_id, self.password, self.first_name, self.last_name, self.phone_number, self.voip

