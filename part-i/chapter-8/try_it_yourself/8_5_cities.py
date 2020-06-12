def describe_city(city_name,country='france'):
    """Display city name and country"""
    print(f"{city_name.title()} is in {country.title()}")

describe_city('lyon')
describe_city('paris')
describe_city('london','england')
