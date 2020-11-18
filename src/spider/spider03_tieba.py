# coding:utf-8

"""
    百度贴吧：https://tieba.baidu.com/f?kw=python3&ie=utf-8&pn=150
        pn:page number
        1 0
        2 50
        3 100
        n (n-1) * 50

    百度搜索：https://www.baidu.com/s?wd=python3&pn=10
        (n - 1) * 10

    复杂的GET请求，多页面下载
"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = 'https://www.baidu.com/s?'

params = {
    'wd': '',
    'pn': 0
}

headers={
    'cookie': 'BIDUPSID=E4045C4E5E6ABB4E2A280A69C94A88E4; PSTM=1605097571; '
              'BAIDUID=E4045C4E5E6ABB4ED8B86950CE4E1D03:FG=1; BD_UPN=12314753; '
              'BDUSS=Y3ekdFWVo5cGhrdzNSY1AwfjJEVEJFcFMxV3Q1Wlp6aGp6Uml6RFhnV2xkOU5mRVFBQUFBJCQAAAAAAAAAAAEAAACU'
              '2sqQaW1haWwyMDE2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKXqq1-'
              'l6qtfMm; BDUSS_BFESS=Y3ekdFWVo5cGhrdzNSY1AwfjJEVEJFcFMxV3Q1Wlp6aGp6Uml6RFhnV2xkOU5mRVFBQUFBJCQAAA'
              'AAAAAAAAEAAACU2sqQaW1haWwyMDE2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKXqq1-l6qtfMm;'
              ' BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=E4045C4E5E6ABB4ED8B86950CE4E1D03:FG=1; '
              'COOKIE_SESSION=18956_0_9_0_33_47_1_0_9_7_1_0_18954_0_2_0_1605515833_0_1605515831%7C9%230_0_1605515831%7C1; '
              '__yjsv5_shitong=1.0_7_c6113396dc09bb9f0e319e07d6364906ada2_300_1605662090507_36.7.154.121_6ab28485; '
              'yjs_js_security_passport=5e4ee5136a8af59349e029280c1d659a3a252f9b_1605662091_js; BD_HOME=1; '
              'H_PS_PSSID=32811_1457_33043_33058_31660_32973_33098_33100_32962; delPer=0; BD_CK_SAM=1; '
              'PSINO=6; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; '
              'H_PS_645EC=0f20LmqqMKLtnhDhNJzRKnfbzMzuAm1wkrndzmZesETAYM6G3oTDzm0e2g5vVxHzZWxx; '
              'BA_HECTOR=2gal202g2484058qpr1fr90a60o; BDSVRTM=136; WWW_ST=1605665103966',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}


def page_get(wd):
    params['wd'] = wd
    for page in range(1, 10):
        params['pn'] = (page - 1) * 10

        page_url = url + urlencode(params)
        print('page_url', page_url)

        response = urlopen(Request(page_url, headers=headers))

        assert response.code == 200

        with open('../../data/baidu_pages/%s-%s.html' % (wd, page), 'wb') as f:
            f.write(response.read())


if __name__ == '__main__':
    page_get('python3')




