import pandas as pd
import matplotlib.pyplot as plt
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
news1 = pd.read_csv("1-8월 뉴스(특수문자 및 불용어 제거).csv", sep=",")
# print(news1.head())
# print(news1.tail())
mediacount=(news1.groupby('media').size().reset_index(name = 'count'))[["media","count"]]
mediacount.to_csv("Media/media(count).csv", mode='w',index=False) #미디어별로 몇개의 기사를 썼는지

# print(news1['media'][0]=="경향신문")
media1=[]
media2=[]
media3=[]
media4=[]
media5=[]
media6=[]
media7=[]
media8=[]
media9=[]
media10=[]

for i in range(len(news1)):
    if (news1['media'][i]=="경향신문"):
        media1.append(news1.iloc[i])
    elif (news1['media'][i]=="국민일보"):
        media2.append(news1.iloc[i])
    elif (news1['media'][i]=="동아일보"):
        media3.append(news1.iloc[i])
    elif (news1['media'][i]=="문화일보"):
        media4.append(news1.iloc[i])
    elif (news1['media'][i]=="서울신문"):
        media5.append(news1.iloc[i])
    elif (news1['media'][i]=="세계일보"):
        media6.append(news1.iloc[i])
    elif (news1['media'][i]=="조선일보"):
        media7.append(news1.iloc[i])
    elif (news1['media'][i]=="중앙일보"):
        media8.append(news1.iloc[i])
    elif (news1['media'][i]=="한겨레"):
        media9.append(news1.iloc[i])
    elif (news1['media'][i]=="한국일보"):
        media10.append(news1.iloc[i])

pd.DataFrame(media1).to_csv("Media/media1.csv",index=0)
pd.DataFrame(media2).to_csv("Media/media2.csv",index=0)
pd.DataFrame(media3).to_csv("Media/media3.csv",index=0)
pd.DataFrame(media4).to_csv("Media/media4.csv",index=0)
pd.DataFrame(media5).to_csv("Media/media5.csv",index=0)
pd.DataFrame(media6).to_csv("Media/media6.csv",index=0)
pd.DataFrame(media7).to_csv("Media/media7.csv",index=0)
pd.DataFrame(media8).to_csv("Media/media8.csv",index=0)
pd.DataFrame(media9).to_csv("Media/media9.csv",index=0)
pd.DataFrame(media10).to_csv("Media/media10.csv",index=0)

print(len(media1)+len(media2)+len(media3)+len(media4)+len(media5)+len(media6)+len(media7)+len(media8)+len(media9)+len(media10))

