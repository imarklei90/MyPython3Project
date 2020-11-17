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
                                         'Cookie':'BIDUPSID=E4045C4E5E6ABB4E2A280A69C94A88E4; PSTM=1605097571; '
                                                  'BAIDUID=E4045C4E5E6ABB4ED8B86950CE4E1D03:FG=1; BD_UPN=12314753; '
                                                  'BDUSS=Y3ekdFWVo5cGhrdzNSY1AwfjJEVEJFcFMxV3Q1Wlp6aGp6Uml6RFhnV2xkOU5mRVFBQUFBJCQAAAAAAAAAAAEAAA'
                                                  'CU2sqQaW1haWwyMDE2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKXqq1-l6qtfMm; '
                                                  'BDUSS_BFESS=Y3ekdFWVo5cGhrdzNSY1AwfjJEVEJFcFMxV3Q1Wlp6aGp6Uml6RFhnV2xkOU5mRVFBQUFBJCQAAAAAAAAAAAEAAACU2s'
                                                  'qQaW1haWwyMDE2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKXqq1-l6qtfMm; '
                                                  'BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=E4045C4E5E6ABB4ED8B86950CE4E1D03:FG=1; '
                                                  'COOKIE_SESSION=18956_0_9_0_33_47_1_0_9_7_1_0_18954_0_2_0_1605515833_0_1605515831%7C9%230_0_1605515831%7C1; '
                                                  'BD_HOME=1; H_PS_PSSID=32811_1457_33043_32945_33058_31660_32973_33098_33100_32962; '
                                                  'DRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=6; '
                                                  'H_PS_645EC=d5d58IsBUiRWpWHFMbz8P2Af6pIpa6pnQ3cTx1D8QndZRKqMSriQzvubfeU; BA_HECTOR=aga501840k0g002rn91fr6u5g0o',
                                         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 '
                                                      'Safari/537.36'

                                    })
    response = urllib.request.urlopen(request)
    print(response.read)
    print(response.code)

    if response.code == 200:
        print('请求成功')

    # 读取响应数据
    bytes_ = response.read()
    with open('%s.html' % wd, 'wb') as f:
        f.write(bytes_)

# 下载一个图片
def download_img(url):

    # 从文件中获取文件名
    filename = url[url.rfind('/') + 1:]

    # 不能下载图片
    #urllib.request.urlretrieve(url, filename)

    req = urllib.request.Request(url, headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 '
                    'Safari/537.36'
    })

    response = urllib.request.urlopen(req)
    # f变量接收的是open函数返回的对象的__enter__()返回的结果
    with open(filename, 'wb') as f:
        f.write(response.read())

    print(f'下载文件{filename} 成功')


if __name__ == '__main__':
    #search_baidu()

    download_img("https://img9.doubanio.com/view/photo/l_ratio_poster/public/p2624391592.jpg")
