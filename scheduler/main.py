from datetime import datetime
import time
import os

from apscheduler.schedulers.blocking import BlockingScheduler

from triggers import pi_temperature

def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    print('Starting Scheduler. %s ' % datetime.now())
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=30)
    scheduler.add_job(pi_temperature.read_pi_temperature, 'interval', seconds=5)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
      scheduler.start()

    except (KeyboardInterrupt, SystemExit):
        pass
