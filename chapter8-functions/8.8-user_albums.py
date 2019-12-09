def make_album(name, title, tracks=0):
    """builds a dictionary describing a music album"""
    album_dict = {
        'artist name': f'{name.title()}',
        'album title': f'{title.title()}'
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


name_prompt = 'Please input the name of the artist:("q" to exit) '
title_prompt = 'Please input the title of the album:("q" to exit) '

while True:
    name = input(name_prompt)
    if name == 'q':
        break
    title = input(title_prompt)
    if title == 'q':
        break
    album = make_album(name, title)
    print(album)

print('Thanks for your respond.')
