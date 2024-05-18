from app.classes.bert_classifier import BertClassifier


class ModelController:
    @staticmethod
    def post(text, model_name):
        model = BertClassifier(model_name)
        label, probabilities = model.predict(text.text)

        return {
            "status": "success",
            "message": "La noticia ha sido clasificada exitosamente.",
            "data": {
                "content": text,
                "classification": bool(label),
                "true_probability": probabilities[1],
                "false_probability": probabilities[0],
            },
        }
