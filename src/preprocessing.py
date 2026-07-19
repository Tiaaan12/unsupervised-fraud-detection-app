import pandas as pd
import numpy as np

def load_process(file_path):
    
    df = pd.read_csv(file_path)

    df.info()
    cols_to_drop = [
    "Unnamed: 0",
    "cc_num",
    "first",
    "last",
    "street",
    "trans_num"
]

    df = df.drop(columns=cols_to_drop, axis=1)

    df['trans_date_trans_time'] = pd.to_datetime(df['trans_date_trans_time'])
    
    df['hour'] = df['trans_date_trans_time'].dt.hour
    df['day'] = df['trans_date_trans_time'].dt.day
    df['month'] = df['trans_date_trans_time'].dt.month
    df['weekday'] = df['trans_date_trans_time'].dt.weekday

    df = df.drop(columns=['trans_date_trans_time'], axis=1)

    df['merchant_freq'] = df['merchant'].map(df['merchant'].value_counts(normalize=True))
    df = df.drop(columns=['merchant', 'city'], axis=1)

    df['job_freq'] = df['job'].map(df['job'].value_counts(normalize=True))
    df = df.drop(columns=['state', 'job'])

    df = pd.get_dummies(df, columns=['category', 'gender'], drop_first=True)

    df = df.drop(columns=['dob'], axis=1)
    return df
