from lib.music_tracker import *

# When we make a music tracker
# it should create an empty list
def test_tracker_starts_empty_list():
    tracker = MusicTracker()
    assert tracker.list_tracks() == []

# We make the music tracker and add one track
# We should see that track in the list
def test_adding_one_track_to_tracker():
    tracker = MusicTracker()
    tracker.add("Many Men by 50 Cent")
    assert tracker.list_tracks() == ["Many Men by 50 Cent"]

# When we have added ultiple tracks to the music tracker
# We should be able to view all those tracks
def test_adding_multiple_tracks():
    tracker = MusicTracker()
    tracker.add("Many Men by 50 Cent")
    tracker.add("Cotton Eyed Joe by Rednex")
    assert tracker.list_tracks() == ["Many Men by 50 Cent", "Cotton Eyed Joe by Rednex"]