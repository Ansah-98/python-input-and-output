import os 
f = open('high.txt', 'w')
players  = ['Ama , 10000' , 'Barney,9000', 'Jane , 8000 ' , 'Fred ,7000']

for p in players :
    f.write( p + '\n')
    
f.close()
