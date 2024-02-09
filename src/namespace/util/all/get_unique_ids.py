import os
import pandas as pd


def get_unique_ids(filepath, column_name):
    df = pd.read_csv(filepath)
        
    unique_ids = df[column_name].unique()
    
    return unique_ids