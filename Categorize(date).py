import pandas as pd
import matplotlib.pyplot as plt
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
news1 = pd.read_csv("1-8월 뉴스(특수문자 및 불용어 제거).csv", sep=",")
# print(news1.head())
# print(news1.tail())

data01=[]
data02=[]
data03=[]
data04=[]
data05=[]
data06=[]
data07=[]
data08=[]
# print(str("2020-01") in (news1['date'][0]))


for i in range(len(news1)):
    if str("2020-01") in (news1['date'][i]):
        data01.append(news1.iloc[i])
    elif str("2020-02") in (news1['date'][i]):
        data02.append(news1.iloc[i])
    elif str("2020-03") in (news1['date'][i]):
        data03.append(news1.iloc[i])
    elif str("2020-04") in (news1['date'][i]):
        data04.append(news1.iloc[i])
    elif str("2020-05") in (news1['date'][i]):
        data05.append(news1.iloc[i])
    elif str("2020-06") in (news1['date'][i]):
        data06.append(news1.iloc[i])
    elif str("2020-07") in (news1['date'][i]):
        data07.append(news1.iloc[i])
    elif str("2020-08") in (news1['date'][i]):
        data08.append(news1.iloc[i])

pd.DataFrame(data01).to_csv("Date/data01.csv",index=0)
pd.DataFrame(data02).to_csv("Date/data02.csv",index=0)
pd.DataFrame(data03).to_csv("Date/data03.csv",index=0)
pd.DataFrame(data04).to_csv("Date/data04.csv",index=0)
pd.DataFrame(data05).to_csv("Date/data05.csv",index=0)
pd.DataFrame(data06).to_csv("Date/data06.csv",index=0)
pd.DataFrame(data07).to_csv("Date/data07.csv",index=0)
pd.DataFrame(data08).to_csv("Date/data08.csv",index=0)
# .to_csv("data01.csv",)
print(len(data01)+len(data02)+len(data03)+len(data04)+len(data05)+len(data06)+len(data07)+len(data08))

