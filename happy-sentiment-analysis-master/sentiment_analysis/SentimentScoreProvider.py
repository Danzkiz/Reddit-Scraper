# External dependencies
from google.cloud import translate
from google.cloud import language
from google.cloud.language import types
from google.cloud.language import enums
import six

class SentimentScoreProvider:
    def __init__(self):
        self.client = language.LanguageServiceClient()

    def analyze(self, content):
        document = types.Document(
            content=content,
            type=enums.Document.Type.PLAIN_TEXT)
        annotations = self.client.analyze_sentiment(document=document)

        return {
                'score': annotations.document_sentiment.score,
                'magnitude': annotations.document_sentiment.magnitude
        }