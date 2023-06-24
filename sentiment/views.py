from rest_framework.views import APIView
from rest_framework.response import Response
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class SentimentAnalysisView(APIView):
    def post(self, request, format=None):
        text = request.data.get('text', '')

        model_name = "StatsGary/setfit-ft-sentinent-eval"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)

        inputs = tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            return_tensors='pt'
        )

        with torch.no_grad():
            logits = model(**inputs)[0]
            predicted_class = torch.argmax(logits).item()
            sentiment = 'positive' if predicted_class == 1 else 'negative' if predicted_class == 0 else 'neutral'

        result = {
            'sentiment': sentiment
        }

        return Response(result)
