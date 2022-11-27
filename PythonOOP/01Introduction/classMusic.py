class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


song_text = 'Battle Hymns \n' +\
            'By moonlight we ride \n' +\
            'Ten thousands \n' +\
            'side by side'
# With swords drawn held high \
# Our whips and armours shine \
# Hail to thee our infantry \
# Still brave beyond the grave \
# All have sworn the eternal vow \
# The time to strike is now \
#     [Chorus:]'
song = Music('Battle Hymns', 'Manowar', song_text)
print(song.print_info())
print(song.play())