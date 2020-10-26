# read in the datafile

filename = 'data/wxobs20170821.txt' 

datafile = open(filename, 'r')  

with open(filename, 'r') as datafile:
     data = datafile.read()  


# DEBUG 
print(data) 
