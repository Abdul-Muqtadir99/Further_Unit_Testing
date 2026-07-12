from lib.music_tracker import *
from lib.track import *

# When we make a music tracker
# it should create an empty list
def test_tracker_starts_empty_list():
    tracker = MusicTracker()
    assert tracker.list_tracks() == []

# We make the music tracker and add one track
# We should see that track in the list
def test_adding_one_track_to_tracker():
    tracker = MusicTracker()
    track1 = Track("Many Men by 50 Cent")
    tracker.add(track1)
    assert tracker.list_tracks() == ["Many Men by 50 Cent"]

# When we have added ultiple tracks to the music tracker
# We should be able to view all those tracks
def test_adding_multiple_tracks():
    tracker = MusicTracker()
    track1 = Track("Many Men by 50 Cent")
    track2 = Track("Cotton Eyed Joe by Rednex")
    tracker.add(track1)
    tracker.add(track2)
    assert tracker.list_tracks() == ["Many Men by 50 Cent", "Cotton Eyed Joe by Rednex"]