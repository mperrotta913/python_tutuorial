from readdata import read_data
from printing import print_comparison
from computation import compute_heatindex


#column names and column indecies to read
columns={'date':0,'time':1,'tempout':2, 'humout':5, 'heatindex':13}

# data types for each column
types={'tempout':float, 'humout':float, 'heatindex':float}



#read data file
data=read_data(columns, types=types)


#compute heatindex
heatindex=[]
for temp, humout in zip(data['tempout'],data['humout']):
    heatindex.append(compute_heatindex(temp,humout))
    


#output
print_comparison('HEATINDEX', data['date'],data['time'], data['heatindex'], heatindex)    






