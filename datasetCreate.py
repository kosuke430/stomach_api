import random
import pandas as pd
import datetime

# データを生成する関数



def generate_data(n):
    #女性の平均の一日消費カロリー
    woman_calory=1430
    #男性の平均の一日消費カロリー

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

        before_eat_time=round(random.uniform(1,23),1)

        before_eat_kind=round(random.uniform(300,800),1)

        after_eat_kind=round(random.uniform(300,800),1)

        if gender=="女性":
            if after_eat_kind+before_eat_kind>(weight*13.397+height*4.799-5.677*age+88.362)*0.8:
                complete_eat=1
            else:
                complete_eat=0
            
        else:
            if after_eat_kind+before_eat_kind-(woman_calory*before_eat_time/24)>(weight*9.247+height*3.098-4.33*age+447.593)*0.8:
                complete_eat=1
            else:
                complete_eat=0
        

            

        

        data.append([age, gender, height, weight,eat_time,before_eat_time,before_eat_kind,after_eat_kind,complete_eat])
    return data

# データを生成
data = generate_data(4000)

# データをDataFrameに変換
df = pd.DataFrame(data, columns=["年齢", "性別", "身長", "体重","今の時間帯","空いた時間","食べたカロリー","これから食べるカロリー","食べれたか"])

# データをCSVファイルに保存
df.to_csv("dataset.csv", index=False)

