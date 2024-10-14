import spacy

class TextExtractor:
    def __init__(self):
        """
        Инициализирует TextExtractor.
        """
        self.nlp = spacy.load("en_core_web_sm")

    def extract_information(self, text):
        doc = self.nlp(text)

        information = {}

        # Извлечение названия метода
        for ent in doc.ents:
            if ent.label_ == "ORG" or "method" in ent.text.lower() or "technique" in ent.text.lower():
                information["name"] = ent.text
                break  # Предполагаем, что название метода упоминается только один раз

        # TODO: Реализовать извлечение другой информации

        return information