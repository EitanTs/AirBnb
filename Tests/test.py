__author__ = 'Ido Bichler'

from Manager.BedManager import BedManager


def test_sanity():
    beds_objects = BedManager('tom', None, None).get_bed_data()
    return beds_objects

if __name__ == '__main__':
    test_sanity()