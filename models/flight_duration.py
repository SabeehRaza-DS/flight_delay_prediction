from datetime import datetime
import pandas as pd
import numpy as np

def flight_duration(df, col1, col2):

    df = df.rename(columns={'DATOP': 'dep_date', 'STD': 'scheduled_time_dep', 'STA': 'scheduled_time_arr',
                     'STATUS': 'Flight_status'})

    if ':' in df[col1][0]:
        df[col1]= pd.to_datetime(df[col1], errors='coerce', format='%Y-%m-%d %H:%M:%S')
    
    elif '.' in df[col1][0]:
        df[col1]= pd.to_datetime(df[col1], errors='coerce', format='%Y-%m-%d %H.%M.%S')

    if ':' in df[col2][0]:
        df[col2]= pd.to_datetime(df[col2], errors='coerce', format='%Y-%m-%d %H:%M:%S')
    
    elif '.' in df[col2][0]:
        df[col2]= pd.to_datetime(df[col2], errors='coerce', format='%Y-%m-%d %H.%M.%S')


    else:
        print('')

    df['flight_duration'] = (df[col2] - df[col1]) / pd.Timedelta(minutes=1)
    
    return df
            
    
    #df['scheduled_dep_time'] = pd.to_datetime(df['scheduled_dep_time'], errors='coerce', format='%Y-%m-%d %H:%M:%S')
    #df[col2] = pd.to_datetime(df['scheduled_arr_time'], errors='coerce', format='%Y-%m-%d %H.%M.%S')

    #(df[col2] - df[col1]) / pd.Timedelta(minutes=1)