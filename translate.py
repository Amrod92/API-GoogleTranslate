from googletrans import Translator

translator = Translator()

def TanslateAPI(text):
    textTranslate = translator.translate(text, dest='en')
    return textTranslate.text