def get_formatted_city(city,country,population=''):
    """Generate city snd country name in defined format"""
    if population:
        city_country =f"{city}, {country} - population {population}"
    else:
        city_country =f"{city}, {country}"
    return city_country.title()