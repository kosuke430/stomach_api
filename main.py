import glob
import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error as mae

files = glob.glob("dataset.csv")

r_file=pd.read_csv("dataset.csv")

data_list = []

for file in files:
    data_list.append(pd.read_csv(file, index_col=0))
df = pd.concat(data_list)

print(r_file.dtypes)

df_train,df_val=train_test_split(df, test_size=0.2)


#データの前処理


#トレーニング処理
col = "食べれたか"
train_y = df_train[col]
train_x = df_train.drop(col, axis=1)

val_y = df_val[col]
val_x = df_val.drop(col, axis=1)

trains = lgb.Dataset(train_x, train_y)
valids = lgb.Dataset(val_x, val_y)

params = {
    "objective": "regression",
    "metrics": "mae"
}

model = lgb.train(params, trains, valid_sets=valids, num_boost_round=1000, early_stopping_rounds=100)