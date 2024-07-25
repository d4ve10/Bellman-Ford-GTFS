import os
import pandas as pd
import numpy as np
from datetime import datetime, time, timedelta

pd.set_option('display.expand_frame_repr', False)

gtfs_dataset = "germany-ic-ice"
# gtfs_dataset = "germany-regional"
# gtfs_dataset = "berlin-vbb"

gtfs_path = os.path.join(os.path.dirname(__file__), '..', 'gtfs', gtfs_dataset)
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', gtfs_dataset + ".csv")


def convert_df_to_np(df):
    np_array = df.to_numpy()
    np_index = dict(zip(df.columns, list(range(0, len(df.columns)))))
    return np_array, np_index


def convert_np_to_dict(np_array, index):
    new_dict = {}
    for key in index:
        new_dict[key] = np_array[index[key]]
    return new_dict
