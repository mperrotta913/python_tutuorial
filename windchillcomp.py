from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import compute_windchill
 
#column names and column indecies to read
columns={'date':0,'time':1,'tempout':2, 'windspeed':7, 'windchill':12}

# data types for each column
types={'tempout':float, 'windspeed':float, 'windchill':float}


#read data from file
data=read_data(columns, types=types)

#computer windchill temperature
windchill=[]
for temp, windspeed in zip(data['tempout'],data['windspeed']):
    windchill.append(compute_windchill(temp,windspeed))
    


#output comparison of data
print_comparison('WINDCHILL',data['date'],data['time'], data['windchill'],windchill)







