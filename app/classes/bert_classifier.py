import torch
from transformers import BertForSequenceClassification, BertTokenizer

class BertClassifier:

    def __init__(self, model_name):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        model = BertForSequenceClassification.from_pretrained(model_name)
        model.to(self.device)
        model.eval()

        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = model

    def predict(self,text,threshold = 0.5):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        inputs.to(self.device)
        with torch.no_grad():
            outputs = self.model(**inputs)

        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1).squeeze().tolist()

        predicted_class = torch.argmax(logits, dim=1).item()
        if probabilities[predicted_class] <= threshold and predicted_class == 1:
            predicted_class = 0

        return predicted_class, probabilities