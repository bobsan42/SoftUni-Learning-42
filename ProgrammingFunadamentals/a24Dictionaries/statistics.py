def statistics():
    stock = {}
    command = input()
    while command != 'statistics':
        inp = command.split(': ')
        key = inp[0]
        val = int(inp[1])
        if key in stock.keys():
            stock[key] += val
        else:
            stock[key] = val
        command = input()

    print('Products in stock:')
    for (key, val) in stock.items():
        print(f"- {key}: {val}")
    print(f'Total Products: {len(stock.keys())}')
    print(f'Total Quantity: {sum(stock.values())}')


statistics()
