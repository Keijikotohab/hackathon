import datetime
import time
import schedule

def job():
    print(datetime.datetime.now())

schedule.every(0.01).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
