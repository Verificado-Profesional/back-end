import pickle
import warnings

import numpy as np
import pandas as pd
import torch
from sentence_transformers import SentenceTransformer, util

from app.config.constants import MODEL_NAME

warnings.simplefilter(action="ignore", category=FutureWarning)


class SentenceSimilarity:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)
        self.news = self.get_news()
        embeddings_array = np.stack(self.news["embeddings"].values)
        self.embeddings = torch.tensor(embeddings_array, dtype=torch.float32)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.embeddings = self.embeddings.to(self.device)

    def save_pickle():
        df = pd.read_csv("./app/data/news_embeddings.csv")
        df["embeddings"] = df["embeddings"].apply(lambda x: np.array(eval(x)))
        with open("./app/data/news.pkl", "wb") as file:
            pickle.dump(df, file)

    def get_news(self):
        with open("./app/data/news.pkl", "rb") as file:
            df = pickle.load(file)
        return df

    def find_similarity(self, query, top_k=5):
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        query_embedding = query_embedding.to(torch.float32)
        query_embedding = query_embedding.to(self.device)

        cos_scores = util.pytorch_cos_sim(query_embedding, self.embeddings)[0]
        top_results = cos_scores.topk(top_k)

        similar_rows = []
        for score, idx in zip(top_results[0], top_results[1]):
            row = self.news.iloc[idx.item()]
            response = {
                "title": row["title"],
                "url": row["url"],
                "source": row["source"],
                "category": row["category"],
                "date": row["date"],
                "score": float(f"{score:.4f}"),
            }
            similar_rows.append(response)

        return similar_rows
