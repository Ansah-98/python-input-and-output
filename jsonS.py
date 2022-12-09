import json

player = {'Anna' : 10000, 'babes': 9000, 'baba' : 8000 }
def serialize(filename, players):
    f = open(filename,'w')
    json.dump( players , f )
    f.close()

serialize('JSON.TXT',player)
