def orders():
    products = {}
    # {product:{price:xx,qty: yy}}

    while True:
        command = input()
        if command == 'buy':
            break
        product, price, qty = command.split(' ')
        if product not in products.keys():
            products[product] = {'price':0.00, 'qty':0}
        products[product]['price'] = float(price)
        products[product]['qty'] += int(qty)

    for product, data in products.items():
        price = data['price']
        qty = data['qty']
        print(f'{product} -> {(price*qty):.2f}')

orders()