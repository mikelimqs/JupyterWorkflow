import os
from urllib.request import urlretrieve

import pandas as pd

URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv', url=URL, force_download=False):
    """Download and cache the fremont data

    Parameters
    __________
    filename : string (optional) 
        location to save data 
    Url : string (optional)
        web location of the data
    forcedownload : bool 
        if true, force dl of data
    Returns
    _______
    pandas.DataFrame
        the fremont bridge data
    """

    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('Fremont.csv', index_col='Date')
    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y %H:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index)
    data.columns = ['West','East']
    data['Total'] = data['West'] + data['East']
    return data
