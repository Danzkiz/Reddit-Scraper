# External dependencies
from google.cloud import translate
import six

class TranslateProvider:
    def __init__(self):
        self.client = translate.Client()
    
    def translate(self, target, text):
        if isinstance(text, six.binary_type):
            text = text.decode('utf-8')
        result = self.client.translate(
             text, target_language=target)

        return result['translatedText']
