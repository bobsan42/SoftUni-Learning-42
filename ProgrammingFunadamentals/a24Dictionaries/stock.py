def stock():
    # stock filling
    some_text = input()
    elements = some_text.split(' ')
    stock = {}
    key = None
    for el in elements:
        if key is None:
            key = el
        else:
            stock[key] = int(el)
            key = None
    # searching for products
    some_text = input()
    elements = some_text.split(' ')
    for x in elements:
        if x in stock.keys():
            print(f'We have {stock[x]} of {x} left')
        else:
            print(f'Sorry, we don\'t have {x}')

stock()