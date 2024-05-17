import torch
import numpy as np
import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer, util
import warnings

MODEL_NAME = 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'
warnings.simplefilter(action='ignore', category=FutureWarning)

class SentenceSimilarity:

    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)
        self.news =  self.get_news()
        embeddings_array = np.stack(self.news['embeddings'].values)
        self.embeddings = torch.tensor(embeddings_array, dtype=torch.float32)
        
    def save_pickle():
        df =  pd.read_csv("./app/data/news_embeddings.csv")
        df['embeddings'] = df['embeddings'].apply(lambda x: np.array(eval(x)))
        with open('news.pkl', 'wb') as file:
            pickle.dump(df, file)
        

    def get_news(self):
        with open("./app/data/news.pkl", 'rb') as file:
            df = pickle.load(file) 
        return df
       
    def find_similarity(self,query, top_k=5):
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        query_embedding = query_embedding.to(torch.float32)

        cos_scores = util.pytorch_cos_sim(query_embedding, self.embeddings)[0]
        top_results = cos_scores.topk(top_k)

        similar_rows = []
        for score, idx in zip(top_results[0], top_results[1]):
            row = self.news.iloc[idx.item()]
            response = {
                "title" : row["title"],
                "url": row["url"],
                "source": row["source"],
                "category": row["category"],
                "date": row["date"],
                "score": float(f"{score:.4f}"),
            } 
            similar_rows.append(response)

        return similar_rows