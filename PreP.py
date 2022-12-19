import pandas as pd

# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
news1 = pd.read_csv("1-8월 뉴스.csv", sep=",")
# print(news1.head()) #데이터프레임 초반부 정보 확인
# print(news1.tail()) #데이터프레임 후반부 정보 확인


stopwords=['무단','전재','무단전재','및','재','배포','재배포','금지']
news1['text']= news1['text'].str.replace("[^ㄱ-하-ㅣ가-힣 ]","") #한글 및 띄어쓰기 이외의 부분 제거
news1['title']= news1['title'].str.replace("[^ㄱ-하-ㅣ가-힣 ]","") #한글 및 띄어쓰기 이외의 부분 제거
print(len(news1))
print(("중복삭제전",news1))
news1=news1.drop_duplicates(['url'], ignore_index = True)
print(len(news1)) #중복데이터 79개 제거
print("중복삭제후",(news1))

for i in range(len(news1)): #데이터 길이
    news1['text'][i] = news1['text'][i].split(" ") #뉴스내용 띄어쓰기 기준으로 분리하여 저장
    news1['text'][i] = [f for f in news1['text'][i] if f not in stopwords] #이후 불용어 제거
    news1['title'][i] = news1['title'][i].split(" ")  # 뉴스제목 띄어쓰기 기준으로 분리하여 저장
    news1['title'][i] = [t for t in news1['title'][i] if t not in stopwords]  # 이후 불용어 제거

    # print(news1)
    # print(news1['text'][i])

print(news1)
news1.to_csv("1-8월 뉴스(특수문자 및 불용어 제거).csv", mode='w',index=0)