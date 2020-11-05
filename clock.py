from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from automater import send_msg
sched = BlockingScheduler()
sched.add_job(send_msg, 'interval', seconds=2)

sched.start()