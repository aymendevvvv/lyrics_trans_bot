from lyricsgenius import Genius
import re  , time  , textwrap
from googletrans import Translator

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

trans = Translator(timeout=1000000 , user_agent=userAgent)

genius = Genius("kAUF2MWRCL4cSD_4PfY3CjiG-npZ0Plt9U-IGL2YCY22-oAKTT0W56abwEzI65sS")


def getLyricsByQuery(query , translate = False)  :
    
    songs = genius.search_songs(query)
    
    if songs['hits'] :
        print("found song on genius")
        id = songs['hits'][0]['result']['id']
        lyrics = genius.lyrics(song_id=id , remove_section_headers=False)
        print(lyrics)

        noHeading = re.sub('\[(.*?)\]' , '' , lyrics)
        
        verses = noHeading.split("\n")
        verses = [element for element in verses[1:-1] if element.strip()]
        versesTrans = trans.translate(noHeading).text.split("\n")
        versesTrans = [element for element in versesTrans[1:-1] if element.strip()]

        first:str = ''
        second:str = ''

        if not translate:
            return [lyrics]
        else:
            result = []
            blockquote_format = "<blockquote>{}</blockquote>\n"

            if len(verses) > 20:
                mid_point = len(verses) // 2
                first = [verse + "\n" + blockquote_format.format(verseTrans) for i, (verse, verseTrans) in enumerate(zip(verses[:mid_point], versesTrans[:mid_point]))]
                second = [verse + "\n" + blockquote_format.format(verseTrans) for i, (verse, verseTrans) in enumerate(zip(verses[mid_point:], versesTrans[mid_point:]))]
                result.extend([first, second])
            else:
                result.extend([verse + "\n" + blockquote_format.format(verseTrans) for verse, verseTrans in zip(verses, versesTrans)])

            return result
        
    else : 
        return []



#print(getLyricsByQuery("neben dir nina chuba" , True))


