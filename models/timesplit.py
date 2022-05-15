



# Split column with timestamps to years, months and extract weekdays
# Input musst be target dataframe and specific column to change as string

import pandas as pd
import numpy as np

def timeSplit(datafra, timeColumn, *args):

    
    
    datafra[timeColumn] = pd.to_datetime(datafra[timeColumn])
    df_years = pd.to_datetime(datafra[timeColumn]).dt.year
    df_months = pd.to_datetime(datafra[timeColumn]).dt.month
    se_weekday = pd.Series([x.weekday() for x in datafra[timeColumn]], name="weekday")
    newPart = np.concatenate((df_years,df_months, se_weekday))
    
    
    if args:
        
        ids = pd.Series(args[0])
        d = {"ID": ids, "year": df_years, "month": df_months, "weekday": se_weekday}
        newPart = pd.DataFrame(data=d)
    
    else:
        d = {"year": df_years, "months": df_months, "weekday": se_weekday}
        newPart = pd.DataFrame(data=d)


    return newPart