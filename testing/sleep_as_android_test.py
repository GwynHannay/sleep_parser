from utils import data_functions as df
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


def test_header():
    """[summary]
    """
    assert df.process_header('Id') == 'id'
    assert df.process_header('Tz') == 'timezone'
    assert df.process_header('From') == 'tracking_start'
    assert df.process_header('To') == 'tracking_end'
    assert df.process_header('Sched') == 'alarm_scheduled'
    assert df.process_header('Hours') == 'tracking_hours'
    assert df.process_header('Rating') == 'rating'
    assert df.process_header('Comment') == 'comment'
    assert df.process_header('Framerate') == 'framerate'
    assert df.process_header('Snore') == 'snore'
    assert df.process_header('Noise') == 'noise'
    assert df.process_header('Cycles') == 'cycles'
    assert df.process_header('DeepSleep') == 'deepsleep'
    assert df.process_header('LenAdjust') == 'lenadjust'
    assert df.process_header('Geo') == 'geo'
    assert df.process_header('19:54') == '19:54'

# def test_dates():
    #assert df.process_dates('tracking_start', '09. 08. 2021 19:49') == '2021-08-09 19:49'
