# This is the start of my own package. Everything is WIP.
# I will be adding more files and folders as I go along.
import pandas as pd

def transformToCat(df, memorySavingThreshold=0.01, check_n_rows=1000):
    """Takes a dataframe and converts all columns of type 'object' to 'category' if the threshold of memory saving is met."""

    try:
        isinstance(df, pd.DataFrame)
        columns = df.select_dtypes(include='object').columns
        new_df = df.copy()

        for column in columns:
            
            old_mem = df.iloc[column,:check_n_rows].nbytes
            new_mem = df[column].astype("category").iloc[:check_n_rows].nbytes
            
            if new_mem < old_mem * (1 - memorySavingThreshold):
                new_df[column] = df[column].astype("category")
        return new_df
    except AttributeError:
        print("The passed argument is not a Dataframe object")
        




#def prepareDf(df, columnsToIgnore=None, maxUniqueValues=100, autoConversionToNumeric=True, 