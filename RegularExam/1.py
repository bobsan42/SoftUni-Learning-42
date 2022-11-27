# ENERGY DRINKS
# https://judge.softuni.org/Contests/Compete/Index/3596#0

mg_of_caffeine = list(map(int,input().split(", ")))
energy_drinks = list(map(int,input().split(", ")))

max_caffeine = 300
Stamat_caffeine = 0
energy_drinks.reverse()

while len(mg_of_caffeine)>0 and len(energy_drinks)>0:
    milligrams = mg_of_caffeine.pop()
    drink = energy_drinks.pop()

    caffeine = milligrams*drink
    if Stamat_caffeine + caffeine <= max_caffeine:
        Stamat_caffeine+= caffeine
    else:
        energy_drinks.reverse()
        energy_drinks.append(drink)
        energy_drinks.reverse()
        Stamat_caffeine -=30
        if Stamat_caffeine <0:
            Stamat_caffeine = 0

if len(energy_drinks)>0:
    energy_drinks.reverse()
    print("Drinks left: ", end="")
    print(", ".join(map(str,energy_drinks)))
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {Stamat_caffeine} mg caffeine.")