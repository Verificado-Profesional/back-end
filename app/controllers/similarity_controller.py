from app.classes.sentence_similarity import SentenceSimilarity
from app.config.config import get_settings

settings = get_settings()


class NewsSimilarityController:
    @staticmethod
    def post(text):
        model = SentenceSimilarity()
        top_similarity = model.find_similarity(text.text)

        return {
            "status": "success",
            "message": "Se obtuvieron exitosamente las noticias similares",
            "data": {
                "content": text,
                "top_results": top_similarity,
            },
        }
