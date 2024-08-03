import requests  




def downloadLinkOnly(youtube_url)->str |None :
     
    headers = {

        'accept': 'application/json',
        'content-type': 'application/json',
         }

    json_data = {
        'url': youtube_url,
        'aFormat': 'mp3',
        'filenamePattern': 'classic',
        'dubLang': False,
        'isAudioOnly': True,
        'isNoTTWatermark': True,
    }

    response = requests.post('https://api.cobalt.tools/api/json', headers=headers, json=json_data)

    return response.json()['url']   



def audioOnlyDownload(youtube_url) -> bytes | None:
    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
    }

    json_data = {
        'url': youtube_url,
        'aFormat': 'mp3',
        'filenamePattern': 'classic',
        'dubLang': False,
        'isAudioOnly': True,
        'isNoTTWatermark': True,
    }

    response = requests.post('https://api.cobalt.tools/api/json', headers=headers, json=json_data)

    if response.status_code == 200:
        resp_url = response.json().get('url')
        if resp_url:
            req_content = requests.get(resp_url)
            if req_content.status_code == 200:
                return req_content.content
            else:
                print("Failed to download the audio content.")
        else:
            print("Response does not contain a valid URL.")
    else:
        print("Something went wrong with the API request.")

    return None

# def save_audio(url):
#     mp3_re = requests.get(audioOnlyDownload(url))

#     # Check if the request was successful (status code 200)
#     if mp3_re.status_code == 200:
#         # Specify the local path where you want to save the MP3 file
#         local_filename = "downloaded.mp3"

#         # Open the local file for writing in binary mode
#         with open(local_filename, 'wb') as f:
#             f.write(mp3_re.content)

#         print(f"File saved as {local_filename}")


#         with open(local_filename, 'rb') as f :
#             return f
#     else:
#         print(f"Failed to download the file. Status code: {mp3_re.status_code}")

#----------------------------------------------------------------------------------------------



