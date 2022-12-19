from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.cluster import DBSCAN
import numpy as np

news1 = pd.read_csv("1-8월 뉴스(특수문자 및 불용어 제거,명사추가).csv", sep=",",index_col=0)

for i in range(len(news1['nouns'])): #news1['nouns']값을 가져올때 data type 이 string으로 읽어오기 때문에 "['a','b','c']" 처럼 생긴 문자열을
    news1['nouns'][i]=eval(news1['nouns'][i])

# 문서를 명사 집합으로 보고 문서 리스트로 치환 (tfidfVectorizer 인풋 형태를 맞추기 위해)
text = [" ".join(noun) for noun in news1['nouns']]
print(text)
tfidf_vectorizer = TfidfVectorizer(min_df = 5, ngram_range=(1,5))
tfidf_vectorizer.fit(text)
vector = tfidf_vectorizer.transform(text).toarray()

vector = np.array(vector) # Normalizer를 이용해 변환된 벡터
model = DBSCAN(eps=0.3,min_samples=6, metric = "cosine")
# 거리 계산 식으로는 Cosine distance를 이용
result = model.fit_predict(vector)

for cluster_num in set(result):
    # -1,0은 노이즈 판별이 났거나 클러스터링이 안된 경우
    if(cluster_num == -1 or cluster_num == 0):
        continue
    else:
        print("cluster num : {}".format(cluster_num))
        temp_news1 = news1[news1['result'] == cluster_num] # cluster num 별로 조회
        for title in temp_news1['title']:
            print(title) # 제목으로 살펴보자
        print()