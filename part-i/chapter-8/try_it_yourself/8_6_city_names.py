def city_country(city_name, country):
    """Return city and country"""
    location =f"{city_name}, {country}"
    return location.title()
    
place=city_country('santiago','chile')
print(place)
place=city_country('paris','france')
print(place)
place=city_country('london','england')
print(place)