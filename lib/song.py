class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment song count
        self.add_song_to_count()

        # Add genre and artist to respective lists
        Song.genres.append(genre)
        Song.artists.append(artist)

        # Update genre and artist counts
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        """Increments the total song count."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        """Ensures genres list contains only unique genres."""
        cls.genres = list(set(cls.genres))  # Remove duplicates

    @classmethod
    def add_to_artists(cls):
        """Ensures artists list contains only unique artists."""
        cls.artists = list(set(cls.artists))  # Remove duplicates

    @classmethod
    def add_to_genre_count(cls):
        """Creates a histogram of song genres."""
        if cls.genre_count.get(cls.genres[-1]):  # Check last added genre
            cls.genre_count[cls.genres[-1]] += 1
        else:
            cls.genre_count[cls.genres[-1]] = 1

    @classmethod
    def add_to_artist_count(cls):
        """Creates a histogram of song artists."""
        if cls.artist_count.get(cls.artists[-1]):  # Check last added artist
            cls.artist_count[cls.artists[-1]] += 1
        else:
            cls.artist_count[cls.artists[-1]] = 1
    pass
