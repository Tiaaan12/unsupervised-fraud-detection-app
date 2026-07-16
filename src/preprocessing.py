import pandas as pd
import numpy as np

def load_process(path: str) -> pd.DataFrame:
    
    data = pd.read_csv(path)
    
    cols_to_drop = {
        "Unnamed: 0",
        "cc_num",
        "first",
        "last",
        "street",
        "trans_num"
    }
    
    data = data.drop(columns=cols_to_drop, axis=1)
