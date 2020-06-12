def make_album(artist_name,album_name):
    """Return dictionary for album info"""
    album=f"{artist_name},{album_name}"
    return album

while True:
    print("\nTell me your favourite artist and album:")
    print("enter 'q' at any time to quit)")
    
    art_name = input("Artist name: ")
    if art_name =='q':
        break
    
    alb_name=input("Album name: ")
    if alb_name == 'q':
        break

    print(f"You love {alb_name} by {art_name}")