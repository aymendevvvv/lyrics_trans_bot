import requests , difflib
from bs4 import BeautifulSoup
from googletrans import Translator


cookies = {
    'PHPSESSID': 'le2qa9s7r7eg2s3ccmmm6c82pk',
    '_gid': 'GA1.2.27592484.1721753720',
    '_au_1d': 'AU1D-0100-001721754568-NZHKQ37C-5STF',
    '_ga_FVWZ0RM4DH': 'GS1.1.1721754881.1.0.1721754881.60.0.0',
    '_gat_gtag_UA_172613_15': '1',
    '__gads': 'ID=7535256d1197ccc2:T=1721753717:RT=1721754886:S=ALNI_MbMVXToGJihZPKv7ORKX6rkDctUOQ',
    '__gpi': 'UID=00000e9dc25065a5:T=1721753717:RT=1721754886:S=ALNI_MY3Sr6hEf4zsjWTTGnrorvgeURjag',
    '__eoi': 'ID=10dbf466b23c3fb1:T=1721753717:RT=1721754886:S=AA-AfjaxsGCykNeezd4FIXn9pbUt',
    'cto_bundle': 'etfbPV8xNHlGWXk2UXloSGhIZkE5R2FiUCUyRlVXTWl4bzk1cHFuWnVMdCUyQndhYllLNFNtQ0g2emhBSmlBV0RvSWpGZ3FhN3o0alhlUEFOa3RkU0hZWHV1TUhaM0VFYXBFc0xrSzJQOUtOZTBjT0VqSEUzUWZvQmJhJTJCMmtQcmJQME4xVGJ3RjhmNk1KMkREZkRSdThyVSUyRlB3UVdkQnRZViUyRnhmYU14Q1hGSHVRRjElMkJ0VWw4b0J6ZUxlNmRwWnI1VFpwNEM4RktkWSUyQnkxJTJGbkZCNlJ2WWRiSG5iZEVuQSUzRCUzRA',
    '_gat_auPassiveTagger': '1',
    '_ga': 'GA1.2.1630937369.1721753717',
    'AWSALB': 'UI0/WB1ge4yPvLnNxFoLRn4eSgv/+wJhgYBgMTJ3WGg8q0We5UJHwU11K6QV5vxxXA2py8XaIFPAmjloAZubSiuqXy1HcUlzQ7MqLLwn5vBBFp07ZP2nyw4vYc/f',
    'AWSALBCORS': 'UI0/WB1ge4yPvLnNxFoLRn4eSgv/+wJhgYBgMTJ3WGg8q0We5UJHwU11K6QV5vxxXA2py8XaIFPAmjloAZubSiuqXy1HcUlzQ7MqLLwn5vBBFp07ZP2nyw4vYc/f',
    '_ga_PSSTD0FYS1': 'GS1.1.1721753719.1.1.1721754901.0.0.0',
    'FCNEC': '%5B%5B%22AKsRol86E7OxZboVLZoHIAKqB3JXw3Q8JV5rvIxFMBoJOhYrLy931Ptmz_OSgUzNtK92GC8Cc7YY12dLp7mqR3thq-UIqf2xacPYn2fmpQbzlfKluGaVSlCwt58_FrDSunfxHvJcuxL4mQFVbaoHHB01yscrTsmW6A%3D%3D%22%5D%5D',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'fr-FR,fr;q=0.9,de-DE;q=0.8,de;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'max-age=0',
    # 'cookie': 'PHPSESSID=le2qa9s7r7eg2s3ccmmm6c82pk; _gid=GA1.2.27592484.1721753720; _au_1d=AU1D-0100-001721754568-NZHKQ37C-5STF; _ga_FVWZ0RM4DH=GS1.1.1721754881.1.0.1721754881.60.0.0; _gat_gtag_UA_172613_15=1; __gads=ID=7535256d1197ccc2:T=1721753717:RT=1721754886:S=ALNI_MbMVXToGJihZPKv7ORKX6rkDctUOQ; __gpi=UID=00000e9dc25065a5:T=1721753717:RT=1721754886:S=ALNI_MY3Sr6hEf4zsjWTTGnrorvgeURjag; __eoi=ID=10dbf466b23c3fb1:T=1721753717:RT=1721754886:S=AA-AfjaxsGCykNeezd4FIXn9pbUt; cto_bundle=etfbPV8xNHlGWXk2UXloSGhIZkE5R2FiUCUyRlVXTWl4bzk1cHFuWnVMdCUyQndhYllLNFNtQ0g2emhBSmlBV0RvSWpGZ3FhN3o0alhlUEFOa3RkU0hZWHV1TUhaM0VFYXBFc0xrSzJQOUtOZTBjT0VqSEUzUWZvQmJhJTJCMmtQcmJQME4xVGJ3RjhmNk1KMkREZkRSdThyVSUyRlB3UVdkQnRZViUyRnhmYU14Q1hGSHVRRjElMkJ0VWw4b0J6ZUxlNmRwWnI1VFpwNEM4RktkWSUyQnkxJTJGbkZCNlJ2WWRiSG5iZEVuQSUzRCUzRA; _gat_auPassiveTagger=1; _ga=GA1.2.1630937369.1721753717; AWSALB=UI0/WB1ge4yPvLnNxFoLRn4eSgv/+wJhgYBgMTJ3WGg8q0We5UJHwU11K6QV5vxxXA2py8XaIFPAmjloAZubSiuqXy1HcUlzQ7MqLLwn5vBBFp07ZP2nyw4vYc/f; AWSALBCORS=UI0/WB1ge4yPvLnNxFoLRn4eSgv/+wJhgYBgMTJ3WGg8q0We5UJHwU11K6QV5vxxXA2py8XaIFPAmjloAZubSiuqXy1HcUlzQ7MqLLwn5vBBFp07ZP2nyw4vYc/f; _ga_PSSTD0FYS1=GS1.1.1721753719.1.1.1721754901.0.0.0; FCNEC=%5B%5B%22AKsRol86E7OxZboVLZoHIAKqB3JXw3Q8JV5rvIxFMBoJOhYrLy931Ptmz_OSgUzNtK92GC8Cc7YY12dLp7mqR3thq-UIqf2xacPYn2fmpQbzlfKluGaVSlCwt58_FrDSunfxHvJcuxL4mQFVbaoHHB01yscrTsmW6A%3D%3D%22%5D%5D',
    'priority': 'u=0, i',
    'referer': 'https://www.lyrics.com/artist.php?name=Kendrick-Lamar&aid=2412704&o=1',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}
userAgent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

trans = Translator(timeout=1000000 , user_agent=userAgent)
def compare (text1:str, text2:str) -> float:
    # Calculate the similarity ratio between two texts
    similarity_ratio = difflib.SequenceMatcher(None, text1, text2).ratio()
    return similarity_ratio

def get_lyrics(url) ->str:
    response = requests.get(url, cookies=cookies, headers=headers)
        
    soup = BeautifulSoup(response.content , "html.parser")
    lyrics_tag = soup.find('pre', {'id': 'lyric-body-text'})
    return lyrics_tag.text

#translated 
def get_lyrics_t(url) :

    lyrics_text = get_lyrics(url=url)

    verses = lyrics_text.split("\n")
    verses = [verse for verse in verses if verse.strip()]

    versesTrans = trans.translate(lyrics_text).text.split("\n")
    versesTrans = [f"<blockquote>{verse}</blockquote>" for verse in versesTrans if verse.strip()]

    result = []

    if len(verses) > 15:
        mid_point = len(verses) // 2
        first = [verse + "\n" + verseTrans for i, (verse, verseTrans) in enumerate(zip(verses[:mid_point], versesTrans[:mid_point]))]
        second = [verse + "\n" + verseTrans for i, (verse, verseTrans) in enumerate(zip(verses[mid_point:], versesTrans[mid_point:]))]
        result.extend([first, second])
    else:
        result.extend([verse + "\n" + verseTrans for verse, verseTrans in zip(verses, versesTrans)])

    return result
    
def get_artists(query) : 
    artists = []
    """ 
    data = {
    'action': 'get_ac',
    'term': f'{query}',
    'type': '1',
    }

    response = requests.post('https://www.lyrics.com/gw.php', cookies=cookies, headers=headers, data=data)
    
    for result in response.json() : 
        if result['category'] == 'Artists' : 
            artists.append((result["term"] , result["link"] , ))

    return artists
 """
    
    response = requests.get(f'https://www.lyrics.com/lyrics/{query}', cookies=cookies, headers=headers, )

    with open("html.html", 'r', encoding='utf-8') as file:
        html_content = file.read()


    soup = BeautifulSoup(response.content, "html.parser")
    

    tbody = soup.find('table')
    tds = tbody.find_all('td')

    for td in tds:
        name = td.find('a', class_='name').text
        link = td.find('a', class_='name')['href']
        artists.append((name , link , ))

    return artists

def get_top_result(query):
    response = requests.get(f'https://www.lyrics.com/lyrics/{query}', cookies=cookies, headers=headers, )
    soup = BeautifulSoup(response.content , "html.parser")
    
    tbody = soup.select_one('#content-body > div > div:nth-child(3)').find('tbody')
    print(tbody)
    tds = tbody.find_all('td')
    #measures similarity
    sim = 0
    print("all artist : ")
    for i  in range(0 , len(tds)) :
        print(tds[i].text)
        currsim = compare( query , tds[i].text)
        if currsim >sim :
            sim = currsim 
            j = i
    
    relv_artist = tds[j]
    songs = get_songs_for(f"https://www.lyrics.com/{relv_artist.select_one('a').get('href')}")
    sim = 0
    relv_song = None
    # removing artist name from query 
    artist_name = relv_artist.text
    words = artist_name.split()
    for word in words :
        query = query.replace(word , "")
    print("all his songs")
    for song in songs :
        currsim = compare(query  , song[0])
        print(song[0] , " -> " , currsim) 
        if currsim > sim :
            sim = currsim
            relv_song = song[1]
    print("most relavent song" , relv_song)
    return 'https://www.lyrics.com'+relv_song


#takes artist profile url and gives back records 
def get_songs_for(artist:str ):
    url_comp = artist.split('/')
    m_url = f'https://www.lyrics.com/artist.php?name={url_comp[-2]}&aid={url_comp[-1]}&o=1'
    response = requests.get(m_url, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text , "html.parser")
    
    tbody_tag = soup.find('div' , class_='tdata-ext').find('tbody')
    result = []
    for song in tbody_tag.find_all('tr'): 
        td_tag = song.find('a')
        result.append((td_tag.text, td_tag.get('href') , ))
    

    return result
#                             [[[[[ api search (not very affective)]]]]]
def search(query) :


    data = {
        'action': 'get_ac',
        'term': query,
        'type': '1',
    }

    response = requests.post('https://www.lyrics.com/gw.php', cookies=cookies, headers=headers, data=data)
    print(response.text)
    return response.json()


print()
for artist in get_artists("kendrick lam") : 
    print(artist[0])
