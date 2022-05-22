import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from collections import Counter

lemmatizer = WordNetLemmatizer()

data = pd.read_csv("scrapped_data.csv")
data.drop("Unnamed: 0", axis = 'columns', inplace = True)

def generate_ngrams(s, n):
    # Convert to lowercases
    s = s.lower()
    
    # Replace all none alphanumeric characters with spaces
    s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)

    # Stopword removal
    stop_words = set(stopwords.words('english'))
    s = " ".join([word for word in str(s).split() if word not in stop_words])

    # Lemmatizing the words
    s = " ".join([lemmatizer.lemmatize(word) for word in s.split()])

    # Break sentence in the token, remove empty tokens
    tokens = [token for token in s.split(" ") if token != ""]
    
    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    ngrams = zip(*[tokens[i:] for i in range(n)])
    final_list = [" ".join(ngram) for ngram in ngrams]

    a = Counter(final_list)
    return a.most_common(5)

def Convert(tup, di = {}):
    di = dict(tup)
    return di

data['article_top_bigrams'] = data['Content'].apply(lambda text: generate_ngrams(text, 2))
data['article_top_bigrams'] = data['article_top_bigrams'].apply(lambda lst: Convert(lst))

data.to_csv("top_bigram.csv",index=False)