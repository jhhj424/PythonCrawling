from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
import os # Miscellaneous operating system interfaces

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요(\',\' 으로 구분하여 다중 검색가능) : ')

searchList = plusUrl.split(',') # ',' 기준으로 문자열 자르기

if not os.path.isdir('downroads'): # downroads 폴더 존재여부 확인 후 없을시 폴더 생성
            os.mkdir('downroads')

for search in searchList:

    # 한글 검색 자동 변환
    search = search.strip()
    url = baseUrl + quote_plus(search)
    html = urlopen(url)
    soup = bs(html, "html.parser")
    img = soup.find_all(class_='_img', limit = 50) # limit: 개수

    n = 1
    for i in img:
        imgUrl = i['data-source']
        with urlopen(imgUrl) as f:
            if not os.path.isdir('downroads/'+search): # 해당 검색어 폴더 존재여부 확인 후 없을시 폴더 생성
                os.mkdir('downroads/'+search)
            with open('downroads/'+search + '/img_' + search + str(n)+'.jpg','wb') as h: # w - write b - binary
                img = f.read()
                h.write(img) # 이미지 write
        n += 1
    print(search + '_다운로드 완료')
