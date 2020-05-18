import subprocess
import logging
logger = logging.getLogger(__name__)

def read_pi_temperature():

  try:
    cmd = ['/usr/bin/vcgencmd', 'measure_temp']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    stdout,stderr = p.communicate()
    logger.info('Reading PI temperature: %s' % stdout)
  except FileNotFoundError as e:
    logger.error(e)
    pass
