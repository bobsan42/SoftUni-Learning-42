def capitals():
    countries = input().split(', ')
    capital_cities = input().split(', ')
    dictionary = {countries[idx]: capital_cities[idx] for idx in range(len(countries))}
    for (country, capital) in dictionary.items():
        print(f'{country} -> {capital}')


# capitals()


def capitals2():
    countries = input().split(', ')
    capital_cities = input().split(', ')
    dictionary = dict(zip(countries, capital_cities))
    for (country, capital) in dictionary.items():
        print(f'{country} -> {capital}')

capitals2()