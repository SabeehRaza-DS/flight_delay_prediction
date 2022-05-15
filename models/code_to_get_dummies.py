import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def code_to_get_dummies(df):

    # 'SXF' is Schonefeld Berlin, dep_country and arr_country empty cell (nan) are connected with 'SXF'
    # therefore fill nan with 'DE' for dep_country and arr_country
    df['dep_country'] = df['dep_country'].replace(np.nan, 'DE')
    df['arr_country'] = df['arr_country'].replace(np.nan, 'DE')
    
    # Based on Arrival and Departure country categorise column as International or National flight
    conditions1 = [df['arr_country'] != df['dep_country'], 
              df['arr_country'] == df['dep_country']]
    choices1 = ['International', 'National']
    df['National_International_Flight'] = np.select(conditions1, choices1)

    # Extracting hours from departure and arrival timestamps
    df['dep_hour'] = df['scheduled_time_dep'].dt.hour
    df['arr_hour'] = df['scheduled_time_arr'].dt.hour


    conditions2 = [(df['dep_hour'] >= 0) & (df['dep_hour'] <= 12),
                    (df['dep_hour'] > 12) & (df['dep_hour'] <= 24)]
    values2 = ['AM', 'PM']
    df['dep_hour'] = np.select(conditions2, values2)

    conditions3 = [(df['arr_hour'] >= 0) & (df['arr_hour'] <= 12),
                    (df['arr_hour'] > 12) & (df['arr_hour'] <= 24)]
    values3 = ['AM', 'PM']
    df['arr_hour'] = np.select(conditions3, values3)


    conditions4 = [(df['dep_hour'] == 'AM') & (df['arr_hour'] == 'AM'),
                    (df['dep_hour'] == 'AM') & (df['arr_hour'] == 'PM'),
                    (df['dep_hour'] == 'PM') & (df['arr_hour'] == 'AM'),
                    (df['dep_hour'] == 'PM') & (df['arr_hour'] == 'PM')]
    choices4 = [1, 2, 3, 4]
    df['AM_PM_flight'] = np.select(conditions4, choices4)


    # Extracting airline name from FLTID column
    df['flight_ID'] = df['FLTID'].str.split().str[0]

    # Extracting aircraft name from AC column
    df['aircraft'] = df['AC'].str.split().str[1]
    df['aircraft_name'] =df['aircraft'].str.slice(0, 3)

    # droping columns ID, dep_date, scheduled_time_dep, scheduled_time_arr

    df = df.drop(columns=['ID', 'dep_date', 'scheduled_time_dep', 'scheduled_time_arr', 
                    'FLTID', 'AC', 'arr_country', 'dep_country', 'dep_hour', 'arr_hour', 'aircraft'], axis=1)

    df['weekday'] = df['weekday'].astype(str)
    df['weekday'] = df['weekday'].astype(str)
    df['AM_PM_flight'] = df['AM_PM_flight'].astype(str)

    df_dummy = pd.get_dummies(df[['month', 'weekday','Flight_status', 
                    'National_International_Flight', 'AM_PM_flight', 'flight_ID', 'aircraft_name']], 
                    drop_first=True)


    df_com = pd.concat([df, df_dummy], axis=1)

    df_com = df_com.drop(columns=['month', 'weekday','Flight_status', 
                    'National_International_Flight', 'AM_PM_flight', 'flight_ID', 'aircraft_name'], 
                    axis=1)
                

    return df_com