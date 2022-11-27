def forecast(*data_tuples):
    forecasts = {}
    weathers = ["Sunny", "Cloudy", "Rainy"]
    for dt in data_tuples:
        location, weather = dt
        if weather not in weathers:
            continue
        forecasts[location] = weathers.index(weather)
    # print(forecasts)
    sorted_cities = dict(sorted(forecasts.items(), key=lambda x: x[0]))
    # return sorted_cities
    # sorted_weathers = sorted(sorted_cities.items(),key=lambda x: weathers.index(x[1])
    weather_sorted = sorted(sorted_cities.items(), key=lambda x: x[1])
    # return weather_sorted
    result = []
    for item in weather_sorted:
        result.append(f'{item[0]} - {weathers[item[1]]}')
    return "\n".join(result)

#
# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))
# print('-'*75)
# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))
# print('-'*75)
# print(forecast(
#     ("Tokyo", "Rainy"),
#     ("Sofia", "Rainy")))
