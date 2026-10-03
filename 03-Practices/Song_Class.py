class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play(self):
        return (f"Playing {self.title} by {self.artist}")

    def get_info(self):
        return f"Title: {self.title}, Artist: {self.artist}, Duration: {self.duration} minutes"

song = Song("Imagine", "John Lennon", 3.1)
print(song.play())
print(song.get_info())
