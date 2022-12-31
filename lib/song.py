class Song:
    pass

    all = []
    genres = []
    artists = []
    count = 0
    artist_count = {}
    genre_count = {}

    def __init__( self, name, artist, genre ):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_to_artists( artist )
        Song.add_to_genres( genre )
        Song.add_song_to_all( self )

    @classmethod
    def add_to_genres( cls, genre ):
        if genre not in cls.genres:
            cls.genres.append( genre.title() )
            cls.genre_count[ genre ] =  1
        else: cls.genre_count[ genre ] += 1

    @classmethod
    def add_to_artists( cls, artist ):
        if artist not in cls.artists:
            cls.artists.append( artist )
            cls.artist_count[ artist ] = 1
        else: cls.artist_count[ artist ] += 1
    
    @classmethod
    def add_song_to_all( cls, song ):
        cls.all.append( song )
        cls.count += 1
