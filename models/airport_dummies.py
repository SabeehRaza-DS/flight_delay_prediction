
import pandas as pd

def airports_dummies(datafra,bins_list,airport_col, *args):

    #if only_binning == False:
    if len(args) == 0: 
        #create bins
        counted_values = datafra[airport_col].value_counts()
        bins = pd.cut(counted_values, bins=bins_list).reset_index()
        bins = bins.rename(columns={"index" : airport_col, airport_col : "Interval"})

        #merge bins to dataframe
        datafra = datafra.merge(bins, on=airport_col)

        #create dummy columns
        dummies = pd.get_dummies(datafra["Interval"], prefix='val', drop_first=True)
        datafra.drop(["Interval"], axis=1, inplace=True)
        datafra = pd.concat([datafra, dummies], axis=1)

        return datafra, bins

    elif len(args) == 1:
        
        bins = args[0]

        #merge bins to dataframe
        datafra = datafra.merge(bins, on=airport_col)

        #create dummy columns
        dummies = pd.get_dummies(datafra["Interval"], prefix='val', drop_first=True)
        datafra.drop(["Interval"], axis=1, inplace=True)
        datafra = pd.concat([datafra, dummies], axis=1)
    

        return datafra