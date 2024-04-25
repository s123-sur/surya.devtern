import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
data = pd.read_csv('news.csv')
a = data['text']
b = data['label']
a_train, a_test, b_train, b_test = train_test_split(a, b, test_size=0.2, random_state=42)
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.5)
tfidf_train = tfidf_vectorizer.fit_transform(a_train)
tfidf_test = tfidf_vectorizer.transform(a_test)
model = PassiveAggressiveClassifier()
model.fit(tfidf_train, b_train)
b_pred = model.predict(tfidf_test)
accuracy = accuracy_score(b_test, b_pred)
confusion = confusion_matrix(b_test, b_pred)
print("Accuracy:", accuracy)
print("Confusion Matrix:\n", confusion)
