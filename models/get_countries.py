import pandas as pd
import numpy as np

def get_countries(dataframe, airports_df):
    list_dep = []
    list_arr = []
    for i in dataframe["DEPSTN"]:
        if i in airports_df["iata"]:
            list_dep.append(airports_df.loc[airports_df['iata'] == i].country[0])
        else:
            list_dep.append("NaN")

    for i in dataframe["ARRSTN"]:
        if i in airports_df["iata"]:
            list_arr.append(airports_df.loc[airports_df['iata'] == i].country[0])
        else:
            list_arr.append("NaN")
    
    df_list_arr = pd.DataFrame(list_arr)
    df_list_arr = df_list_arr.rename(columns={0: 'arr_country'})

    df_list_dep = pd.DataFrame(list_dep)
    df_list_dep = df_list_dep.rename(columns={0: 'dep_country'})

    dataframe = pd.concat([dataframe, df_list_arr, df_list_dep], axis=1)
    
    return dataframe