import os
import pandas as pd
import numpy as np

df = pd.read_csv('plates/labels.info',sep='\n',names=['filepath'])
label_df = pd.DataFrame({'filepath':df['filepath'].iloc[::2].values, 'platenum':df['filepath'].iloc[1::2].values})
filename = 'data-path.txt'
label_df.to_csv(path_or_buf='train-path.txt',sep=' ', index=False, header=False)
