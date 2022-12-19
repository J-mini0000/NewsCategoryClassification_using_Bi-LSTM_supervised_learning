#파일이름 toknize라고 짓지 말것... 아래 페이지와 같은 오류가 남
#https://stackoverflow.com/questions/64807163/importerror-cannot-import-name-from-partially-initialized-module-m
import pandas as pd

news1 = pd.read_csv("1-8월 뉴스(특수문자 및 불용어 제거,명사추가).csv", sep=",",index_col=0)

drop_index_list = []  # 지워버릴 index를 담는 리스트
for i, row in news1.iterrows():
    temp_nouns = row['nouns']
    if len(temp_nouns) == 0:  # 만약 명사리스트가 비어 있다면
        drop_index_list.append(i)  # 지울 index 추가

news1 = news1.drop(drop_index_list)  # 해당 index를 지우기

# index를 지우면 순회시 index 값이 중간중간 비기 때문에 index를 다시 지정
news1.index = range(len(news1))

print(drop_index_list)
