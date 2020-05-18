from datetime import datetime
import time
import os
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


from apscheduler.schedulers.blocking import BlockingScheduler

from triggers import pi_temperature

def tick():
    logger.info('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    logger.info('Starting Scheduler. %s ' % datetime.now())
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=30)
    scheduler.add_job(pi_temperature.read_pi_temperature, 'interval', seconds=5)
    logger.info('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
      scheduler.start()

    except (KeyboardInterrupt, SystemExit):
        pass
