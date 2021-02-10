import glob
import pandas as pd

data = pd.DataFrame()
for file_name in glob.glob("./data/" + '*.csv'):
    new_data = pd.read_csv(file_name, low_memory=False)
    data = pd.concat([data, new_data], axis=0)

data.to_csv('./ROCStories.tsv', sep='\t')
