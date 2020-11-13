


#column names and column indecies to read

columns={'date':0,'time':1,'tempout':2, 'windspeed':7, 'windchill':12}

# data types for each column

types={'tempout':float, 'windspeed':float, 'windchill':float}


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


#computer windchill temperature

def compute_windchill(t,v):
    a=35.74
    b=.6215
    c=35.75
    d=.4275

    v16=v**.16

    wci=a+(b*t)-(c*v16)+(d*t*v16)
    return wci



#running the fuction to compute windchill temperature
windchill=[]

for temp, windspeed in zip(data['tempout'],data['windspeed']):
    windchill.append(compute_windchill(temp,windspeed))
    


#output
print('                Original  Computed')
print(' Date    Time  Windchill Windchill Difference')
print('------- ------ --------- --------- ----------')
zip_data=zip(data['date'],data['time'],data['windchill'],windchill)

for date, time, wc_orig, wc_comp in zip_data:
    wc_diff=wc_orig-wc_comp
    print(f'{date} {time:>4} {wc_orig:9.6f} {wc_comp:8.4f} {wc_diff:10.6f}')
    







