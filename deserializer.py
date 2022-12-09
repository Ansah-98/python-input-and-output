

def deserialize(filename,players):
    f = open(filename,"r")

    for entry in f :
        split = entry.split(',')
        name = split[0]
        score = split[1]
        players[name] = score
    f.close()

play = {}
deserialize('high.txt', play)   
print(play)