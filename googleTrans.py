from googletrans import Translator

trans = Translator()

text:str = "hallo wie geht's "

print(trans.translate(text).text)