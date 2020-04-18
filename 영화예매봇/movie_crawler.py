import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

# Telegram Bot 생성
my_token = '839037088:AAG_AJZ5iQXsMSDgXtFIagWxdHRbbhkbUF8'
bot = telegram.Bot(token = my_token)

# 크롤링 대상
url = 'http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200417'

# Main 로직
def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')

    if(imax):
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id=824661375, text= title + ' IMAX 예매가 열렸습니다.')
        sched.pause()

# 30초마다 실행하는 반복 스케쥴러
sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=30)
sched.start()