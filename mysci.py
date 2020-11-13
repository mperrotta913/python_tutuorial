


#column names and column indecies to read

columns={'date':0,'time':1,'tempout':2, 'windspeed':7}

# data types for each column

types={'tempout':float, 'windspeed':float}


#initalizing a data variable
data={}
for column in columns:
    data[column]=[]



#read data file

filename="data/wxobs20170821.txt"


with open(filename, 'r') as datafile:      # 'with' provides cleanup an ensures the file is closed at the end  

    # read the first 3 lins (header) of the file
    for _ in range(3):
        datafile.readline()
        


    # read and parse the rest of the file
    for line in datafile:
        split_line=line.split()
        for column in columns:
            i=columns[column]
            t=types.get(column, str)
            value=t(split_line[i])
            data[column].append(value)



