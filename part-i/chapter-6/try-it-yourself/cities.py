cities={
    'lagos':{
        'country':'nigeria',
        'population':'20m',
        'fact':'economic capital',
        },
    'paris':{
        'country':'france',
        'population':'6m',
        'fact':'the eiffel tower is here',
        },
    'london':{
        'country':'england',
        'population':'5m',
        'fact':'the queen lives here most times',
        },
    }
for city, info in cities.items():
    print(f"\n{city.title()}:")
    country = info['country']
    population = info['population']
    fact = info['fact']
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population.title()}")
    print(f"\tFact: {fact.title()}")