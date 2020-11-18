# coding: utf-8

"""
    豆瓣音乐
        url：https://music.douban.com/artists/tag/%E6%B5%81%E8%A1%8C?page=3
        page = n

"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode


url = 'https://music.douban.com/artists/tag/%E6%B5%81%E8%A1%8C?'

param = {
    'page': ''
}

headers = {
    'Cookie': 'll="118183"; bid=XDRWz0AqshE; __utmc=30149280; __utma=30149280.1425209625.1605665432.1605665432.1605665432.1; '
              '__utmz=30149280.1605665432.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; '
              '_vwo_uuid_v2=DF2FD98530856C660E5871CFE2A85BC73|e3677dd357f0499687889a3cbdd6f24d; '
              'gr_user_id=11c088eb-9e19-466d-97be-e8133a7f5070; '
              'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=c4c369cc-6ec8-43bc-944c-3b7f3b0ad9fa; '
              'gr_cs1_c4c369cc-6ec8-43bc-944c-3b7f3b0ad9fa=user_id%3A0; '
              'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_c4c369cc-6ec8-43bc-944c-3b7f3b0ad9fa=true; '
              '_pk_ref.100001.afe6=%5B%22%22%2C%22%22%2C1605665857%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; '
              '_pk_ses.100001.afe6=*; _pk_id.100001.afe6=3586fcc98c7e36d6.1605665857.1.1605665898.1605665857.; '
              '__utmb=30149280.9.10.1605665432',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 '
                  'Safari/537.36'
}


def get_music():
    for i in range(1, 11):
        param['page'] = i
        page_url = url + urlencode(param)
        print('page_url:', page_url)

        response = urlopen(Request(page_url, headers=headers))

        assert response.code == 200

        with open('../../data/douban/music/%s.html' % i, 'wb') as f:
            f.write(response.read())


if __name__ == '__main__':
    get_music()
