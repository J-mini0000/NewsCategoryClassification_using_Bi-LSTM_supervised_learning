import pandas as pd
import matplotlib.pyplot as plt
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
news1 = pd.read_csv("1-8월 뉴스.csv", sep=",",index_col=0)
# print(news1.head())
# print(news1.tail())
# stopwords=['무단','전재','및','재','배포','재배포','금지']
# news1['text']= news1['text'].str.replace("[^ㄱ-하-ㅣ가-힣 ]","") #한글 및 띄어쓰기 이외의 부분 제거
#
# news1.to_csv("1-8월 뉴스(특수문자 제거).csv", mode='w')

# plt.rcParams["font.family"]="NanumGothic"
# news1['media'].value_counts().plot(kind ='bar')

