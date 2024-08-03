from googletrans import Translator

trans = Translator()

text:str = " hola me amigos"

print(trans.translate(text).text)