__author__ = 'Ido Bichler'

from Manager.BedManager import BedManager
from Manager.LoginManager import LoginManager


def test_sanity():

    print LoginManager('tom', '1234356789').is_valid()

if __name__ == '__main__':
    test_sanity()