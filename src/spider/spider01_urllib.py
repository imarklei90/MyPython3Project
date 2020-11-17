# coding:utf-8

import urllib
import urllib.request
from urllib.parse import quote


def search_baidu(wd='中国'):
    url = 'https://www.baidu.com/s?wd=%s'

    # response = urllib.request.urlopen(url % urllib.parse.quote(wd))

    # 生成请求对象，封装请求的url和header
    request = urllib.request.Request(url % quote(wd),
                                     headers={
                                         'Cookie': "E4045C4E5E6ABB4E2A280A69C94A88E4; PSTM=1605097571; BAIDUID=E4045C4E5E6ABB4ED8B86950CE4E1D03:FG=1; BD_UPN=12314753; "
                                                   "BDUSS=Y3ekdFWVo5cGhrdzNSY1AwfjJEVEJFcFMxV3Q1Wlp6aGp6Uml6RFhnV2xkOU5mRVFBQUFBJCQAAAAAAAAAAAEAAACU2sqQaW1haWwyMDE2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKXqq1-l6qtfMm; "
                                                   "BDUSS_BFESS=Y3ekdFWVo5cGhrdzNSY1AwfjJEVEJFcFMxV3Q1Wlp6aGp6Uml6RFhnV2xkOU5mRVFBQUFBJCQAAAAAAAAAAAEAAACU2sqQaW1haWwyMDE2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKXqq1-l6qtfMm; "
                                                   "BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ",
                                                   "H_PS_PSSID=32811_1457_33043_32945_33058_31660_32973_32705_33098_33100_32962; delPer=0; BD_CK_SAM=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BD_HOME=1; COOKIE_SESSION=1780_0_9_0_31_39_1_2_7_7_1_4_1783_0_5_0_1605321933_0_1605321928%7C9%230_0_1605321928%7C1; PSINO=5; "
                                                   "H_PS_645EC=7356MX%2BNGtzIKFiGOOVpzb9UOVeAV5inzRdmyg%2BLt4BcRXrw9Zc7qUKpYQs; BA_HECTOR=8ka10k002g2h85agpf1fqukgf0p"
                                         'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
                                     })
    response = urllib.request.urlopen(request)
    print(response.read)
    print(response.code)

    #assert response.code == 200
    print('请求成功')

    # 读取响应数据
    bytes_ = response.read()
    with open('%s.html' % wd, 'wb') as f:
        f.write(bytes_)


if __name__ == '__main__':
    search_baidu()
