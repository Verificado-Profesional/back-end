from app.classes.bert_classifier import BertClassifier

def predict_text(model,text):
    label, probabilities = model.predict(text)
    response =  {
        "content": text,
        "classification": bool(label),
        "true_probability": probabilities[1],
        "false_probability": probabilities[0],
    }
    return response

class ModelController:
    @staticmethod
    def post(text, model_name):
        model = BertClassifier(model_name)

        parsed_text = text.text.replace('\n\n', ' [SEP] ')
        predicted_text = predict_text(model,parsed_text)
        predicted_text["content"] = text.text

        paragraphs = text.text.split('\n')
        predicted_paragraphs = []
        for paragraph in paragraphs:
            if paragraph:
                predicted_paragraph = predict_text(model,paragraph)
                predicted_paragraphs.append(predicted_paragraph)

        return {
            "status": "success",
            "message": "La noticia ha sido clasificada exitosamente.",
            "data": {
                "predicted_text":predicted_text,
                "predicted_paragraphs":predicted_paragraphs,
            },
        }

    