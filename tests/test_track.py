from lib.track import *

def test_adding_one_track():
    track1 = Track("Many Men by 50 Cent")
    assert track1.get_track() == "Many Men by 50 Cent"