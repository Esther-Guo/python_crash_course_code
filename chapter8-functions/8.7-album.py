def make_album(name, title, tracks=0):
    """builds a dictionary describing a music album"""
    album_dict = {
        'artist name': f'{name.title()}',
        'album title': f'{title.title()}'
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


album = make_album('Taylor Swift', 'reputation')
print(album)

album = make_album('coldplay', 'ghost story')
print(album)

album = make_album('one republic', 'native', 11)
print(album)
