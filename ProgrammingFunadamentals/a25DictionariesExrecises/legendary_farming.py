def legendary_farming():
    # items = {
    #     'Shadowmourne': {'required_material': 'shards', 'required_qty': 250},
    #     'Valanyr': {'required_material': 'fragments', 'required_qty': 250},
    #     'Dragonwrath': {'required_material': 'motes', 'required_qty': 250},
    # }  # item : {material, target_qty}
    material_targets = {
        'shards': {'required_qty': 250, 'prize': 'Shadowmourne'},
        'fragments': {'required_qty': 250, 'prize': 'Valanyr'},
        'motes': {'required_qty': 250, 'prize': 'Dragonwrath'},
    }
    collected = {'shards':0,'fragments':0,'motes':0}
    junk = {}
    prize_won = False
    while not prize_won:
        some_input = input().split(' ')
        for i in range(0, len(some_input), 2):
            material = some_input[i + 1].lower()
            qty = int(some_input[i])

            if material not in material_targets.keys():
                if material not in junk.keys():
                    junk[material] = 0
                junk[material] += qty
                continue
            else:
                # if material not in collected.keys():
                #     collected[material] = 0
                collected[material] += qty

            required_qty = material_targets[material]['required_qty']
            prize = material_targets[material]['prize']

            if collected[material] >= required_qty:
                collected[material] -= required_qty
                print(f'{prize} obtained!')
                prize_won = True
                break
            # print(collected, junk)

    for (mat, qty) in collected.items():
        print(f'{mat}: {qty}')
    for (mat, qty) in junk.items():
        print(f'{mat}: {qty}')


legendary_farming()
