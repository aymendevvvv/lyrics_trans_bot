import requests , re , eyed3 , sys 
from geniuslyrics import *

eyed3.log.setLevel("ERROR")
def getId(down_url):
    
    url = down_url
    pattern = r'(?:v=|\/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)

    if match:
        video_id = match.group(1)
        return video_id

def getDownUrl(youtube_link):
    headers = {
        'authority': 'co.wuk.sh',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://cobalt.tools',
        'referer': 'https://cobalt.tools/',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }

    json_data = {
        'url': f"https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D{getId(youtube_link)}",
        'aFormat': 'mp3',
        'filenamePattern': 'classic',
        'dubLang': False,
        'isAudioOnly': True,
        'isNoTTWatermark': True,
    }

    response = requests.post('https://co.wuk.sh/api/json', headers=headers, json=json_data)
    print("Download url : ", response.json()["url"])
    return response.json()["url"]

def save_audio(url):
    mp3_re = requests.get(getDownUrl(url))

    # Check if the request was successful (status code 200)
    if mp3_re.status_code == 200:
        # Specify the local path where you want to save the MP3 file
        local_filename = "downloaded.mp3"

        # Open the local file for writing in binary mode
        with open(local_filename, 'wb') as f:
            f.write(mp3_re.content)

        print(f"File saved as {local_filename}")


        with open(local_filename, 'rb') as f :
            return f
    else:
        print(f"Failed to download the file. Status code: {mp3_re.status_code}")

def get_audio(url):

    save_audio(url)
    return open("downloaded.mp3" , 'rb')
#----------------------------------------------------------------------------------------------



def get_title(file_path):
    audiofile = eyed3.load(file_path)
    
    if audiofile.tag:
        return audiofile.tag.title.split("(")[0]
        
    
#link = input("insert the youtube link :")
#save_audio(link)


