import sys

from sklearn.preprocessing import LabelEncoder
import pickle
import pandas as pd

get_data={
    '年齢': int(sys.argv[1]),
    '性別': sys.argv[2],
    '身長': float(sys.argv[3]),
    '体重': float(sys.argv[4]),
    '今の時間帯': int(sys.argv[5]),
    '空いた時間': float(sys.argv[6]),
    '食べたカロリー': float(sys.argv[7]),
    'これから食べるカロリー': float(sys.argv[8])
}


#モデルのパラメータをロード
load_model_lightGBM=pickle.load(open('stomach_api/parameter.sav','rb'))

df_single = pd.DataFrame([])

le = LabelEncoder()
sexlabels=['女性','男性']
sexlabels_id=le.fit_transform(sexlabels)

df_single = pd.DataFrame([get_data])
df_single['hour'] = df_single['今の時間帯']
df_single['性別'] = le.transform(df_single['性別'])
df_single.drop('今の時間帯', axis=1, inplace=True)

X_single = df_single

pred_prob = load_model_lightGBM.predict(X_single, num_iteration=load_model_lightGBM.best_iteration)
prediction = 1 if pred_prob[0] >= 0.5 else 0

if prediction == 1:
    print("食事を完食する可能性が高いです")
else:
    print("完食しない可能性が高いです")