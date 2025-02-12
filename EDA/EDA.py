# the data is clean therefor no need to transform the data

import pandas as pd

# Import AwsDataHandler to get the data from aws
from aws_handler import AwsDataHandler

# # get the path/file from aws
# data_handler = AwsDataHandler(aws_file_path='data/predictive-maintenance/clean_data/clean_data.parquet')
# aws_path = data_handler.get_data_from_aws()


local_path = 'data/aircraft engine/PM_train.parquet'
df = pd.read_parquet(local_path)

# for i in df.columns.tolist():
#     print(i, ': ', df[i].nunique())

## many columns with only 1 unique value:

# we should try dropping them and make model
# s6 with 2 unique value only it has 2 unique value let see

print(df['s6'].describe())

# the value is float not a int which odd cuz 2 unique value + the diff in value is 0.01 let see more

