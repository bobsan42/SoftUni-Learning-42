def miner_task():
    dictionary = {}
    command = input()
    i = 1
    res = ''
    qty = 0
    while command != 'stop':
        if i % 2==1:
            res = command
        else:
            qty = int(command)
            if not res in dictionary.keys():
                dictionary[res] = 0
            dictionary[res] += qty
        command = input()
        i +=1

    for (res, qty) in dictionary.items():
        print(f'{res} -> {qty}')



miner_task()