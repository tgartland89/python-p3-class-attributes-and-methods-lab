class Song:
    pass

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
# Clears ERROR lib/testing/song_test.py - TypeError: Song() takes no arguments
# Interrupted: 1 error during collection

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
# Clears ERROR lib/testing/song_test.py - AttributeError: 'Song' object has no attribute 'add_song_to_count'

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
# Clears ERROR lib/testing/song_test.py - AttributeError: 'Song' object has no attribute 'add_to_genres'

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
# Clears ERROR lib/testing/song_test.py - AttributeError: 'Song' object has no attribute 'add_to_artists'

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
# Clears ERROR lib/testing/song_test.py - AttributeError: 'Song' object has no attribute 'add_to_genre_count'

    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
#  Clears ERROR lib/testing/song_test.py - AttributeError: 'Song' object has no attribute 'add_to_artist_count'

# all the above clears all of this 
# Class "Song" in song.py instantiates with a name, artist, and genre. .                                                                                  
# Class "Song" in song.py counts the total number of Song objects. .                                                                                   
# Class "Song" in song.py keeps track of all Song genres. .                                                                                                
# Class "Song" in song.py keeps track of all Song artists. .                                                                                               
# Class "Song" in song.py keeps count of Songs for each genre. .
# Class "Song" in song.py keeps count of Songs for each artist. .