from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

news1 = pd.read_csv("1-8월 뉴스(특수문자 및 불용어 제거,명사추가).csv", sep=",",index_col=0)

# 문서를 명사 집합으로 보고 문서 리스트로 치환 (tfidfVectorizer 인풋 형태를 맞추기 위해)
text = [" ".join(noun) for noun in news1['nouns']]
print(text)
tfidf_vectorizer = TfidfVectorizer(min_df = 5, ngram_range=(1,5))
tfidf_vectorizer.fit(text)
vector = tfidf_vectorizer.transform(text).toarray()