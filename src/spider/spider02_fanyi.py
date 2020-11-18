# coding:utf-8

"""
    百度翻译

"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import json

url = 'https://fanyi.baidu.com/sug'

headers={
    'cookie': 'BIDUPSID=E4045C4E5E6ABB4E2A280A69C94A88E4; PSTM=1605097571; BAIDUID=E4045C4E5E6ABB4ED8B86950CE4E1D03:FG=1; '
             'BDUSS=Y3ekdFWVo5cGhrdzNSY1AwfjJEVEJFcFMxV3Q1Wlp6aGp6Uml6RFhnV2xkOU5mRVFBQUFBJCQAAAAAAAAAAAEAAACU2sqQaW1haW'
             'wyMDE2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKXqq1-l6qtfMm; '
             'BDUSS_BFESS=Y3ekdFWVo5cGhrdzNSY1AwfjJEVEJFcFMxV3Q1Wlp6aGp6Uml6RFhnV2xkOU5mRVFBQUFBJCQAAAAAAAAAAAEAAACU2s'
             'qQaW1haWwyMDE2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKXqq1-l6qtfMm; '
             'BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=E4045C4E5E6ABB4ED8B86950CE4E1D03:FG=1; '
             'H_PS_PSSID=32811_1457_33043_32945_33058_31660_32973_33098_33100_32962; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; '
             'delPer=0; PSINO=6; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1605602794; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; '
             'FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1605603590;'
             ' __yjsv5_shitong=1.0_7_c6113396dc09bb9f0e319e07d6364906ada2_300_1605603590918_36.7.154.121_e8a832fb; '
             'yjs_js_security_passport=d369c62abe3d9823d0383100987a4ce4cb8c6240_1605603592_js',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}


def fanyi(kw):
    data = {
        'kw': kw
    }

    req = Request(url, data=urlencode(data).encode('utf-8'))
    resp = urlopen(req)
    assert resp.code == 200

    json_data = resp.read()
    print(resp.read)
    #print(content_type)
    return json.loads(json_data.decode('utf-8'))


if __name__ == '__main__':
    print(fanyi('中国'))




