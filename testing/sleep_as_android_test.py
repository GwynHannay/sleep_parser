import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import data_functions as df

def test_header():
    assert df.process_header('Tz') == 'timezone'

#def test_dates():
    #assert df.process_dates('tracking_start', '09. 08. 2021 19:49') == '2021-08-09 19:49'