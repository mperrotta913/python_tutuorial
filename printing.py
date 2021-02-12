

def print_comparison(name, dates, times, original_data, computed_data):
    """
    print a comparison of two time series (original and computed)

    Parameters
        name: a string name for the data being compared (limited to 9 character in length)
        dates: list of strings representing dates of each data
        times: list of string representing times of each data
        original_data: list of original data (floats)
        computed_data: list of computed data (float)
    """

    #output comparison of data
    print('                Original  Computed')
    print(f' Date    Time  {name.upper():>9} {name.upper():>9} Difference')
    print('------- ------ --------- --------- ----------')
    zip_data=zip(dates, times ,original_data,computed_data)

    for date, time, orig, comp in zip_data:
        diff=orig-comp
        print(f'{date} {time:>4} {orig:9.6f} {comp:8.4f} {diff:10.6f}')
