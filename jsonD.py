import json 

def deserializer(filename):
    f = open(filename,'r')
    players = json.load(f)
    f.close()


    return players 

print(deserializer('JSON.TXT'))