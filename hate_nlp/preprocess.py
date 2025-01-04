import re
import nltk
from unidecode import unidecode
import string

class Preprocessor:

    def __call__(self, df):
        assert 'text' in df
        return self.preprocess(df)

    def preprocess(self, df):
        return df

class PreprocessToldBR(Preprocessor):
    def __init__(self):
        self.stopwords = list(set([unidecode(w) for w in nltk.corpus.stopwords.words('portuguese')]))

    def preprocess(self, df):
        df["text"] = df["text"].apply(lambda x: re.sub("#[^ ]+", "", x)) # remove hashtags
        df["text"] = df["text"].apply(lambda x: re.sub(r"\d+", "", x)) # remove numbers
        df["text"] = df["text"].apply(lambda x: x.translate(str.maketrans("", "", string.punctuation))) # remove punctuation
        df["text"] = df["text"].apply(lambda x: unidecode(x)) # remove accents
        df["text"] = df["text"].apply(lambda x: re.sub("http[^ ]+", "", x)) # remove links
        df["text"] = df["text"].apply(lambda x: " ".join(w.strip() for w in x.split() if w not in self.stopwords)) # remove stopword

        return df


    