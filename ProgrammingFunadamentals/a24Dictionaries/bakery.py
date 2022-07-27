some_text = input()
elements = some_text.split(' ')
bakery={}
key = None
for el in elements:
    if key is None:
        key = el
    else:
        bakery[key] = int(el)
        key =None
print(bakery)
