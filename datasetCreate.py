import random
import pandas as pd
import datetime

# データを生成する関数
def generate_data(n):
    data = []
    for _ in range(n):
        age = random.randint(18, 80)
        gender = random.choice(["男性", "女性"])
        if gender=='女性':
            height = 155+round(random.uniform(0,100)/10, 1)
        else:
            height = 165+round(random.uniform(0,100)/10, 1)

        weight =round((height*height*22)/10000+random.uniform(0,10)/10,1)

        now = datetime.datetime.now()
        eat_time= now.replace(hour=random.randint(1,23), minute=random.randint(1,59), second=0, microsecond=0)

        before_eat_time=random.uniform(1,23)

        before_eat_kind=random.uniform(0,800)

        after_eat_kind=

        data.append([age, gender, height, weight])
    return data

# データを生成
data = generate_data(4000)

# データをDataFrameに変換
df = pd.DataFrame(data, columns=["年齢", "性別", "身長", "体重",])

# データをCSVファイルに保存
df.to_csv("dataset.csv", index=False)

