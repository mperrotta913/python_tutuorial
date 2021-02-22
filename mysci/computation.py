def compute_windchill(t,v):
    """
    compute the windchill factor given the temperature and windspeed
    
    Note: this computation is only valid for temperatures betweeen -45F and +45F
          and for windspeeds between 3 mph and 60 mph
    Parameters
    t: the temperature in units of F (float)
    v: the wind speed in units of mph (foat)
    """

    a=35.74
    b=.6215
    c=35.75
    d=.4275

    v16=v**.16

    wci=a+(b*t)-(c*v16)+(d*t*v16)
    return wci


def compute_heatindex(t, hum):
    """
    compute heat index given temperature and humidity

    Parameters
    t: temperature in units of F (float0
    hum: relative humidity in units of % (flaot)
    """

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

def compute_dewpoint(t,h):
    """
    compute the dewpoint temperature given temperature and humidity

    Parameters
    t: temperature in units F (float)
    h: the relative humidity in units % (float)
    """

    tempc=(t-32)/(5/9) #convert temperature from degree F to degree C
    rh=h/100


    b=18.678
    c=257.14 #deg C

    gamma=math.log(rh)+(b*tempc)/(c+tempc)
    tdp=c*gamma/(b-gamma)

    tdp_F=(9/5)*tdp+32 #convert deg C to deg F
    return tdp_F



    


