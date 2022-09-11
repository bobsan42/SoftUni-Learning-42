players = {}
matches = {}

def challenger():
    while True:
        command = input()
        if command == 'Season end':
            break
        data = command.split(' -> ')
        if len(data) >1:
            player = data[0]
            position = data[1]
            skill = int(data[2])
            if player not in players.keys():
                players[player] = {}#{'position':'','skill':0}
            if position not in players[player].keys():
                players[player]={position:0,'total':0}
            if players[player][position] < skill:
                players[player][position] = skill
        else:
            data=command.split(' vs ')
            left_player = data[0]
            right_player = data[1]
            if left_player not in players.keys():
                continue
            if right_player not in players.keys():
                continue
            

