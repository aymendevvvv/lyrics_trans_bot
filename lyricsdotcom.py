import requests
from bs4 import BeautifulSoup
'''
    ## need to scrape with beautiful soup later , better results ##
'''
cookies = {
    'PHPSESSID': '0hcuiacvl0pskfv6un9srqtr26',
    '_uc_referrer': 'https://www.reddit.com/',
    '_gid': 'GA1.2.1171095024.1705076082',
    '_au_1d': 'AU1D-0100-001705076154-6ECFOLBL-79RZ',
    'DAPROPS': '"bS:0|scsVersion:2.4.5|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdeviceAspectRatio:1366/768|sdevicePixelRatio:1|idisplayColorDepth:24|sdownlink:5.15|seffectiveConnectionType:4g|bflashCapable:0|bhtml.audio.ogg:1|bhtml.audio.mp3:1|bhtml.audio.wav:1|bhtml.audio.m4a:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video.ap4x:0|bhtml.video.av1:1|bhtml.video.ogg:1|bhtml.video.h264:1|bhtml.video.webm:1|bjs.accessDom:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.webGl:1|sjs.webGlRenderer:ANGLE (Intel, Intel(R) UHD Graphics 620 (0x00005917) Direct3D11 vs_5_0 ps_5_0, D3D11)|bjs.webSockets:1|bjs.webSqlDatabase:0|bjs.webWorkers:1|bjs.xhr:1|srendererRef:0236014205|iroundTripTime:150|bsaveData:0|sscreenWidthHeight:1366/768|stimeZone:Africa/Lagos|buserMedia:1|sch.bitness:64|sch.browserFullVersionList:%22Not_A%20Brand%22%3Bv%3D%228.0.0.0%22%2C%20%22Chromium%22%3Bv%3D%22120.0.6099.217%22%2C%20%22Google%20Chrome%22%3Bv%3D%22120.0.6099.217%22|sch.browserList:%22Not_A%20Brand%22%3Bv%3D%228%22%2C%20%22Chromium%22%3Bv%3D%22120%22%2C%20%22Google%20Chrome%22%3Bv%3D%22120%22|sch.model:|sch.platform:%22Windows%22|sch.platformVersion:%2210.0.0%22|splatformArchitecture:x86|srequestingMobileUx:false|saudioRef:781311942|bmouseActivity:1bE:0"',
    '_pbjs_userid_consent_data': '3524755945110770',
    '_lr_retry_request': 'true',
    '_lr_env_src_ats': 'false',
    'pbjs-unifiedid': '%7B%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222024-01-12T16%3A15%3A59%22%7D',
    'pbjs-unifiedid_last': 'Fri%2C%2012%20Jan%202024%2016%3A15%3A58%20GMT',
    'panoramaId_expiry': '1705680959459',
    '_cc_id': 'ec7862325a70812d471e9cfcc7d7541',
    'panoramaId': '3fd50b2552be9f3c8b632c56641916d5393802754ea4de3baefe39ebfed09b5b',
    '_au_last_seen_pixels': 'eyJhcG4iOjE3MDUwNzYxNTQsInR0ZCI6MTcwNTA3NjE1NCwicHViIjoxNzA1MDc2MTU0LCJydWIiOjE3MDUwNzYxNTQsInRhcGFkIjoxNzA1MDc2MTU0LCJhZHgiOjE3MDUwNzYxNTQsImdvbyI6MTcwNTA3NjE1NCwiY29sb3NzdXMiOjE3MDUwNzYxNTQsImFkbyI6MTcwNTA3NjE1NCwiaW1wciI6MTcwNTA3NjE1NCwic21hcnQiOjE3MDUwNzYxNjUsInVucnVseSI6MTcwNTA3NjE2NSwiYW1vIjoxNzA1MDc2MTY1LCJzb24iOjE3MDUwNzYxNjUsIm9wZW54IjoxNzA1MDc2MTY1LCJiZWVzIjoxNzA1MDc2MTY1LCJ0YWJvb2xhIjoxNzA1MDc2MTY1LCJwcG50IjoxNzA1MDc2MTY1fQ%3D%3D',
    '__gads': 'ID=491671c03721f7ed:T=1705076084:RT=1705078002:S=ALNI_Mb95EQmiP58KjPskiR5f2Xdkv6Unw',
    '__gpi': 'UID=00000cf4b889c6c3:T=1705076084:RT=1705078002:S=ALNI_Max5q5i7BhXtGFwEUmzIhf9yRIh_Q',
    'AWSALB': 'UiPlT0+nw7r6N2D5wnC6g+6ChOH/rNfBpzoCtwcUEZBxfLaY8/bVHWbAnCErROkMluxB0MCvsFtOkQR9M9kRv5sbZtU0ZZOxn5HlBp23iY6vgdTywsqwfreB0jmZ',
    'AWSALBCORS': 'UiPlT0+nw7r6N2D5wnC6g+6ChOH/rNfBpzoCtwcUEZBxfLaY8/bVHWbAnCErROkMluxB0MCvsFtOkQR9M9kRv5sbZtU0ZZOxn5HlBp23iY6vgdTywsqwfreB0jmZ',
    '_ga': 'GA1.2.2061274602.1705076082',
    '_ga_PSSTD0FYS1': 'GS1.1.1705076081.1.1.1705078058.0.0.0',
    'FCNEC': '%5B%5B%22AKsRol8ZNeiUvUTj9R7AbP05AHOTnl6Pcd3ZCdY52vtTaph0EcPZ417Yf0QWSGS--MlYEfGSwEphuGhuAF_QA1SBACBtyfBR2B7fuvFD61DvYHJmV6NWN67BgUjE27518M6bE_HMzXv7xGmKa9T_Ub5j58ApBVhUIw%3D%3D%22%5D%2Cnull%2C%5B%5B5%2C%2281%22%5D%5D%5D',
}

headers = {
    'authority': 'www.lyrics.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'PHPSESSID=0hcuiacvl0pskfv6un9srqtr26; _uc_referrer=https://www.reddit.com/; _gid=GA1.2.1171095024.1705076082; _au_1d=AU1D-0100-001705076154-6ECFOLBL-79RZ; DAPROPS="bS:0|scsVersion:2.4.5|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdeviceAspectRatio:1366/768|sdevicePixelRatio:1|idisplayColorDepth:24|sdownlink:5.15|seffectiveConnectionType:4g|bflashCapable:0|bhtml.audio.ogg:1|bhtml.audio.mp3:1|bhtml.audio.wav:1|bhtml.audio.m4a:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video.ap4x:0|bhtml.video.av1:1|bhtml.video.ogg:1|bhtml.video.h264:1|bhtml.video.webm:1|bjs.accessDom:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.webGl:1|sjs.webGlRenderer:ANGLE (Intel, Intel(R) UHD Graphics 620 (0x00005917) Direct3D11 vs_5_0 ps_5_0, D3D11)|bjs.webSockets:1|bjs.webSqlDatabase:0|bjs.webWorkers:1|bjs.xhr:1|srendererRef:0236014205|iroundTripTime:150|bsaveData:0|sscreenWidthHeight:1366/768|stimeZone:Africa/Lagos|buserMedia:1|sch.bitness:64|sch.browserFullVersionList:%22Not_A%20Brand%22%3Bv%3D%228.0.0.0%22%2C%20%22Chromium%22%3Bv%3D%22120.0.6099.217%22%2C%20%22Google%20Chrome%22%3Bv%3D%22120.0.6099.217%22|sch.browserList:%22Not_A%20Brand%22%3Bv%3D%228%22%2C%20%22Chromium%22%3Bv%3D%22120%22%2C%20%22Google%20Chrome%22%3Bv%3D%22120%22|sch.model:|sch.platform:%22Windows%22|sch.platformVersion:%2210.0.0%22|splatformArchitecture:x86|srequestingMobileUx:false|saudioRef:781311942|bmouseActivity:1bE:0"; _pbjs_userid_consent_data=3524755945110770; _lr_retry_request=true; _lr_env_src_ats=false; pbjs-unifiedid=%7B%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222024-01-12T16%3A15%3A59%22%7D; pbjs-unifiedid_last=Fri%2C%2012%20Jan%202024%2016%3A15%3A58%20GMT; panoramaId_expiry=1705680959459; _cc_id=ec7862325a70812d471e9cfcc7d7541; panoramaId=3fd50b2552be9f3c8b632c56641916d5393802754ea4de3baefe39ebfed09b5b; _au_last_seen_pixels=eyJhcG4iOjE3MDUwNzYxNTQsInR0ZCI6MTcwNTA3NjE1NCwicHViIjoxNzA1MDc2MTU0LCJydWIiOjE3MDUwNzYxNTQsInRhcGFkIjoxNzA1MDc2MTU0LCJhZHgiOjE3MDUwNzYxNTQsImdvbyI6MTcwNTA3NjE1NCwiY29sb3NzdXMiOjE3MDUwNzYxNTQsImFkbyI6MTcwNTA3NjE1NCwiaW1wciI6MTcwNTA3NjE1NCwic21hcnQiOjE3MDUwNzYxNjUsInVucnVseSI6MTcwNTA3NjE2NSwiYW1vIjoxNzA1MDc2MTY1LCJzb24iOjE3MDUwNzYxNjUsIm9wZW54IjoxNzA1MDc2MTY1LCJiZWVzIjoxNzA1MDc2MTY1LCJ0YWJvb2xhIjoxNzA1MDc2MTY1LCJwcG50IjoxNzA1MDc2MTY1fQ%3D%3D; __gads=ID=491671c03721f7ed:T=1705076084:RT=1705078002:S=ALNI_Mb95EQmiP58KjPskiR5f2Xdkv6Unw; __gpi=UID=00000cf4b889c6c3:T=1705076084:RT=1705078002:S=ALNI_Max5q5i7BhXtGFwEUmzIhf9yRIh_Q; AWSALB=UiPlT0+nw7r6N2D5wnC6g+6ChOH/rNfBpzoCtwcUEZBxfLaY8/bVHWbAnCErROkMluxB0MCvsFtOkQR9M9kRv5sbZtU0ZZOxn5HlBp23iY6vgdTywsqwfreB0jmZ; AWSALBCORS=UiPlT0+nw7r6N2D5wnC6g+6ChOH/rNfBpzoCtwcUEZBxfLaY8/bVHWbAnCErROkMluxB0MCvsFtOkQR9M9kRv5sbZtU0ZZOxn5HlBp23iY6vgdTywsqwfreB0jmZ; _ga=GA1.2.2061274602.1705076082; _ga_PSSTD0FYS1=GS1.1.1705076081.1.1.1705078058.0.0.0; FCNEC=%5B%5B%22AKsRol8ZNeiUvUTj9R7AbP05AHOTnl6Pcd3ZCdY52vtTaph0EcPZ417Yf0QWSGS--MlYEfGSwEphuGhuAF_QA1SBACBtyfBR2B7fuvFD61DvYHJmV6NWN67BgUjE27518M6bE_HMzXv7xGmKa9T_Ub5j58ApBVhUIw%3D%3D%22%5D%2Cnull%2C%5B%5B5%2C%2281%22%5D%5D%5D',
    'referer': 'https://www.lyrics.com/lyrics/immer%20kalt',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

def get_lyrics():
    response = requests.get('https://www.lyrics.com/lyric-lf/5914866/AYLIVA/Immer+kalt', cookies=cookies, headers=headers)
        
    soup = BeautifulSoup(response.content , "html.parser")
    lyrics_tag = soup.find('pre', {'id': 'lyric-body-text'})
    print(lyrics_tag.text)
    
def search(query) :

    data = {
        'action': 'get_ac',
        'term': query,
        'type': '1',
    }

    response = requests.post('https://www.lyrics.com/gw.php', cookies=cookies, headers=headers, data=data)
    return response.json()