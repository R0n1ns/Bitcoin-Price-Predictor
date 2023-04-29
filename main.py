import pandas as pd
from data_load import data_proc

dt = data_proc(data_loc='dataset.csv',cat=['Value_Classification'])
