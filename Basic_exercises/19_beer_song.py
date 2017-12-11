"""
"99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips,
as it has a very repetitive
format which is easy to memorize, and can take a long time to sing. The song's simple lyrics are as follows:
99 bottles of beer on the wall, 99 bottles of beer.
Take one down, pass it around, 98 bottles of beer on the wall.
The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers reach zero.
Your task here is write a Python program capable of generating all the verses of the song.
"""


def get_beer_song():
    count = 99
    full_song = []
    lyrics = """{0} bottles of beer on the wall, {0} bottles of beer.
Take one down, pass it around, {1} bottles of beer on the wall."""
    while count > 0:
        full_song.append(lyrics.format(count, count - 1))
        count -= 1
    return full_song

if __name__ == "__main__":
    fantastic_song = get_beer_song()
    for verse in fantastic_song:
        print(verse)
