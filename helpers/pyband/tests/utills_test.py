from pyband.utils import parse_epoch_time
from datetime import datetime


def test_parse_datetime_to_epoch():
    raw_datetime = "2020-11-05T09:15:18.445494105Z"
    assert parse_epoch_time(raw_datetime) == 1604567718


def test_parse_epoch_to_datetime():
    raw_datetime = "2020-11-05T09:15:18.445494105Z"
    assert datetime.utcfromtimestamp(parse_epoch_time(raw_datetime)) == datetime(2020, 11, 5, 9, 15, 18)
