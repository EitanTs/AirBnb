__author__ = 'Ido Bichler'

from Manager.BedManager import BedManager


def test_sanity():
    beds_objects = BedManager('tom', '19/06/2017', '20/06/2017').get_relevant_beds_scores()
    return beds_objects

if __name__ == '__main__':
    test_sanity()