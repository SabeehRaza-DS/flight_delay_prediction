import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

def code_plot(df):

    df['day_name'] = df['dep_date'].dt.day_name()

    # 'SXF' is Schonefeld Berlin, dep_country and arr_country empty cell (nan) are connected with 'SXF'
    # therefore fill nan with 'DE' for dep_country and arr_country
    df['dep_country'] = df['dep_country'].replace(np.nan, 'DE')
    df['arr_country'] = df['arr_country'].replace(np.nan, 'DE')

    # Based on Arrival and Departure country categorise column as International or National flight
    conditions = [df['arr_country'] != df['dep_country'], 
              df['arr_country'] == df['dep_country']]

    choices = ['International', 'National']

    df['National_International_Flight'] = np.select(conditions, choices)

    # Extracting hours from departure and arrival timestamps
    df['dep_hour'] = df['scheduled_time_dep'].dt.hour
    df['arr_hour'] = df['scheduled_time_arr'].dt.hour

    conditions1 = [(df['dep_hour'] >= 0) & (df['dep_hour'] <= 12),
                    (df['dep_hour'] > 12) & (df['dep_hour'] <= 24)]
    values1 = ['AM', 'PM']
    df['dep_AM/PM'] = np.select(conditions1, values1)

    conditions2 = [(df['arr_hour'] >= 0) & (df['arr_hour'] <= 12),
                    (df['arr_hour'] > 12) & (df['arr_hour'] <= 24)]
    values2 = ['AM', 'PM']
    df['arr_AM/PM'] = np.select(conditions2, values2)

    # Extracting Aircraft name from AC column
    df['AC'] =df['AC'].str.slice(0, 6)

    # Extracting flight ID name from FLTID column
    df['flight_ID'] = df['FLTID'].str.split().str[0]

    df = df.drop(columns=['ID', 'dep_date','scheduled_time_dep', 'scheduled_time_arr'], 
                axis=1)
                
    return df