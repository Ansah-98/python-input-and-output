players = {"Anna" : 10000, "Barney": 9000 , "Jane": 8000, 'Fred': 7000}

def serialize(filename,players):
    f = open(filename,'w')

    for p in players:
        f.write(p + ',' +str(players[p]) + '\n')

    f.close()

serialize('high.txt', players)