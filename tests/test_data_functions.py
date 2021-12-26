from datetime import datetime
from utils import data_functions as df
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


def test_suffix():
    assert df.process_suffix(datetime(2021, 8, 1, 8, 6)) == '2021-08'


def test_pk():
    assert df.process_pk('1614539708475') == 1614539708475


def test_dates():
    assert df.process_dates('09. 08. 2021 19:49') == '2021-08-09 19:49'


def test_float():
    assert df.process_float('1.24') == 1.24


def test_integer():
    assert df.process_integer('123456') == 123456


def test_actigraphy():
    assert df.process_actigraphy('19:54', '8.419333', datetime(2021, 8, 1, 8, 6)) == {
        'actigraphic_time': '2021-08-01 19:54',
        'actigraphic_value': '8.419333'
    }

    assert df.process_actigraphy('02:02', '9.999', datetime(2021, 8, 1, 8, 6)) == {
        'actigraphic_time': '2021-08-02 02:02',
        'actigraphic_value': '9.999'
    }


def test_event():
    assert df.process_event('DHA-1628509755221') == {
        'event_type': 'DHA',
        'event_time': '2021-08-09 19:49:15.221'
    }

    assert df.process_event('DHA-1628509755307-2.75506E-40') == {
        'event_type': 'DHA',
        'event_time': '2021-08-09 19:49:15.307',
        'event_value': '2.75506E-40'
    }

    assert df.process_event('AWAKE_END-1628509758612') == {
        'event_type': 'AWAKE_END',
        'event_time': '2021-08-09 19:49:18.612'
    }

    assert df.process_event('LUX-1628509758613-228.19624') == {
        'event_type': 'LUX',
        'event_time': '2021-08-09 19:49:18.613',
        'event_value': '228.19624'
    }

    assert df.process_event('HR-1628509905221-96.0') == {
        'event_type': 'HR',
        'event_time': '2021-08-09 19:51:45.221',
        'event_value': 96.0
    }


def test_array():
    assert df.process_array(['leaf', 'tree']) == '["leaf", "tree"]'
