favourite_places = {
    'diane':['paris','new york','chicago'],
    'rainbow':['los angeles','istanbul'],
    'tony':['lagos','dubai','london'],
    }

for person,places in favourite_places.items():
    print(f"{person}'s favourite places are: ")
    for place in places:
     print(f"\t{place}")