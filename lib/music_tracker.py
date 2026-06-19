class MusicTracker:
    def __init__(self):
        self.tracks = []
    
    def add(self, track):
        return self.tracks.append(track)

    def list_tracks(self):
        return self.tracks