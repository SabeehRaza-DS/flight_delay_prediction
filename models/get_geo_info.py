from matplotlib.pyplot import axis
import pandas as pd
import numpy as np

def get_geo_info(dataframe, airports_df):

    geo_info = airports_df[["iata", "country"]].reset_index().drop("index", axis=1).rename(columns={"iata" : "DEPSTN",})
    geo_info.insert(1, "ARRSTN", geo_info.DEPSTN)
    df_prep = dataframe.merge(geo_info.drop("ARRSTN", axis=1), how="left", on="DEPSTN").rename(columns={"country" : "dep_country", "elevation" : "dep_elev", "lat" : "dep_lat", "lon" : "dep_lon", "tz" : "dep_tz"})
    df_final = df_prep.merge(geo_info.drop("DEPSTN", axis=1), how="left", on="ARRSTN").rename(columns={"country" : "arr_country", "elevation" : "arr_elev", "lat" : "arr_lat", "lon" : "arr_lon", "tz" : "arr_tz"})

    #df_final = df_final.drop(["arr_country", "dep_country"], axis = 1)

    return df_final