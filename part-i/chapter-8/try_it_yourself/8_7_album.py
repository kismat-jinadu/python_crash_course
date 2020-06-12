def make_album(artist_name,album_name):
    """Return dictionary for album info"""
    album={'artist':artist_name,'album':album_name}
    return album

music=make_album('beyonce','dangerously in love')
print(music)

music=make_album('linkin park','hybrid theory')
print(music)

music=make_album('sir','chasing summer')
print(music)

def make_album(artist_name,album_name,number_songs=None):
    """Return dictionary for album info"""
    album={'artist':artist_name,'album':album_name}
    if number_songs:
        album['number_songs']=number_songs
    return album

music=make_album('beyonce','dangerously in love')
print(music)

music=make_album('linkin park','hybrid theory')
print(music)

music=make_album('sir','chasing summer',number_songs=14)
print(music)