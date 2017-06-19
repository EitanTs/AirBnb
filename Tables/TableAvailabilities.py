from Tables.Table import Table


class TableAvailabilities(Table):

    TABLE_NAME = 'Rooms'

    def __init__(self, bed_id, date, renter_id):
        super(TableAvailabilities, self).__init__(self.TABLE_NAME)
        self.bed_id = bed_id
        self.date = date
        self.renter_id = renter_id

    @property
    def values(self):
        return self.bed_id, self.date, self.renter_id

