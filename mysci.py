#read data file

filename="data/wxobs20170821.txt"


with open(filename, 'r') as datafile:      # 'with' provides cleanup an ensures the file is closed at the end  
	data=datafile.read()



