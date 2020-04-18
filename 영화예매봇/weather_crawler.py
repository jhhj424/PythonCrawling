import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

# Telegram Bot 생성
my_token = '839037088:AAG_AJZ5iQXsMSDgXtFIagWxdHRbbhkbUF8'
bot = telegram.Bot(token = my_token)

# 크롤링 대상
url = 'https://www.weatheri.co.kr/forecast/forecast01.php?rid=0202020102&k=1&a_name=%EA%B3%A0%EC%96%91'

# Main 로직
# def job_function():
html = requests.get(url)
html.raise_for_status()
 
html.encoding=None   # None 으로 설정
#resp.encoding='euc-kr'  # 한글 인코딩

soup = BeautifulSoup(html.text, 'html.parser')
weather = soup.select('body > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(2) > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(1) > td > table > tbody > tr > td > b > font')
print(weather)

# 10초마다 실행하는 반복 스케쥴러
# sched = BlockingScheduler()
# sched.add_job(job_function, 'interval', seconds=10)
# sched.start()
