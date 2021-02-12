from readdata import read_data


#column names and column indecies to read
columns={'date':0,'time':1,'tempout':2, 'humout':5, 'heatindex':13}

# data types for each column
types={'tempout':float, 'humout':float, 'heatindex':float}


#initalizing a data variable
data={}
for column in columns:
    data[column]=[]



#read data file
data=read_data(columns, types=types)


#compute heatindex
def compute_heatindex(t, hum):
    a=-42.379
    b=2.04901523
    c=10.14333127
    d=0.22475541
    e=0.00683783
    f=0.05481717
    g=.00122874
    h=0.00085282
    i=0.00000199

    rh= hum/100

    hi=(a+(b*t)+(c*rh)+(d*t*rh)+(e*t**2)+(f*rh**2)+(g*t**2*rh)+(h*t*rh**2)+(i*t**2*rh**2))

    return hi

#running the fuction to compute heatindex
heatindex=[]

for temp, humout in zip(data['tempout'],data['humout']):
    heatindex.append(compute_heatindex(temp,humout))
    


#output
print('                Original  Computed')
print(' Date    Time  HEAT INDEX HEAT INDEX Difference')
print('------- ------ --------- --------- ----------')
zip_data=zip(data['date'],data['time'],data['heatindex'],heatindex)

for date, time, hi_orig, hi_comp in zip_data:
    hi_diff=hi_orig-hi_comp
    print(f'{date} {time:>4} {hi_orig:9.6f} {hi_comp:8.4f} {hi_diff:10.6f}')
    






