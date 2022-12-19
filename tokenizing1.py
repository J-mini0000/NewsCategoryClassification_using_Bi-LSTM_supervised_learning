#파일이름 toknize라고 짓지 말것... 아래 페이지와 같은 오류가 남
#https://stackoverflow.com/questions/64807163/importerror-cannot-import-name-from-partially-initialized-module-m
import pandas as pd
from konlpy.tag import Okt

okt=Okt()
nouns=[]

newsname=['경향신문','국민일보','문화일보','서울신문','세계일보','조선일보','중앙일보','한겨레','한국일보','동아일보','권범철','서민호']
stopwords=['무단','전재','무단전재','및','재','배포','재배포','금지','권범철', '기자', '그림판', '바로가기']
stopwords=stopwords+newsname
for j in newsname:
    nntk = okt.nouns(j)
    for k in range(len(nntk)):
        stopwords.append(nntk[k])
stopwords=list(set(stopwords))

news1 = pd.read_csv("1-8월 뉴스(특수문자 및 불용어 제거).csv", sep=",",index_col=0)
for i in range(len(news1['text'])):
    token= okt.nouns(news1['text'][i])
    print("token1", token)
    token = [t for t in token if t not in stopwords]
    print("token2", token)
    nouns.append(token)
    print(i/len(news1['text'])*100,"%")
print(nouns)
news1['nouns']=nouns
print(news1.head())

drop_index_list = []  # 지워버릴 index를 담는 리스트
for i, row in news1.iterrows():
    temp_nouns = row['nouns']
    if len(temp_nouns) == 0:  # 만약 명사리스트가 비어 있다면
        drop_index_list.append(i)  # 지울 index 추가

news1 = news1.drop(drop_index_list)  # 해당 index를 지우기

# index를 지우면 순회시 index 값이 중간중간 비기 때문에 index를 다시 지정
news1.index = range(len(news1))

news1.to_csv("1-8월 뉴스(특수문자 및 불용어 제거,명사추가).csv", mode='w',index=0)