

def read_data(columns, types={},filename="data/wxobs20170821.txt"):
    """
    this area is for notes on the script without the restriction of 1 line that '#' has. for this script, 

    read data from CU Boulder Weather station data file

    Parameters:
    columns: A dictionary of column names mapping to column indices
    types: A dictionary of column names mapping to the types to which to convert each column of data
    filename: A string path pointing to the CU Boulder weather station data file
    """


    #initalizing a data variable
    data={}
    for column in columns:
        data[column]=[]



    #read data file
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



    return data
