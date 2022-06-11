from math import ceil

distance_to_the_moon = 384400  # km
time_spent_on_the_moon = 3  # hours

velocity = float(input())
fuel_consumption = float(input())  # litres/100 km

time_to_fly_one_way = distance_to_the_moon / velocity
total_time = ceil(2 * time_to_fly_one_way + time_spent_on_the_moon)
fuel_needed = int(2 * distance_to_the_moon * fuel_consumption / 100)

print(total_time)
print(fuel_needed)
