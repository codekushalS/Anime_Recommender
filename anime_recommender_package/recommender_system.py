import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer

class anime_recommender:
    def __init__(self, dataset_path):
        self.data = pd.read_csv(dataset_path)
        self.preprocess_data()

    def stem_sentences(self, sentence):
        tokens = sentence.split()
        ps = PorterStemmer()
        stemmed_tokens = [ps.stem(token) for token in tokens]
        return ' '.join(stemmed_tokens)
    
    def preprocess_data(self):
        self.data.drop_duplicates(inplace=True)
        self.data['synopsis'].fillna(' ', inplace=True)
        self.data['genre'] = self.data['genre'].str.replace(" ", "")
        self.data['genre'] = self.data['genre'].str.replace('[', '', regex=True).str.replace('\'', '', regex=True).str.replace(']', '', regex=True).str.replace(',', ' ', regex=True)
        self.data['synopsis'] = self.data['synopsis'].str.replace('\n', '', regex=True)
        self.data['tags'] = self.data['genre'] + ' ' + self.data['synopsis']
        self.data['tags'] = self.data['tags'].str.replace('[Written by MAL Rewrite]', '', regex=False)
        self.data['tags'] = self.data['tags'].str.lower()
        self.data = self.data[['uid', 'title', 'tags']]
        self.data['tags'] = self.data['tags'].apply(self.stem_sentences)
        cv = CountVectorizer(max_features=5000, stop_words='english')
        self.vectors = cv.fit_transform(self.data['tags']).toarray()
        self.sim = cosine_similarity(self.vectors)

    def recommend(self, anime):
        anime_index = self.data[self.data['title'] == anime].index[0]
        distances = self.sim[anime_index]
        anime_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recs = [self.data.iloc[i[0]]['title'] for i in anime_list]

        return recs
        


    
        