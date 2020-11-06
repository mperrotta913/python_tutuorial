#initalizing a data variable
data={'date':[],'time':[],'tempout':[]}




#read data file

filename="data/wxobs20170821.txt"


with open(filename, 'r') as datafile:      # 'with' provides cleanup an ensures the file is closed at the end  

    # read the first 3 lins (header) of the file
    for _ in range(3):
        datafile.readline()

    # read and parse the rest of the file
    for line in datafile:
        split_line=line.split()
        data['date'].append(split_line[0])
        data['time'].append(split_line[1])
        data['tempout'].append(float(split_line[2]))


