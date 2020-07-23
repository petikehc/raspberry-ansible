
import logging
import re
import subprocess
from mqtt import client as mqtt_client
logger = logging.getLogger(__name__)

def read_pi_temperature():

  try:
    cmd = ['/usr/bin/vcgencmd', 'measure_temp']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    stdout,stderr = p.communicate()
    match = re.match(r'temp=(.*)\'C', str(stdout, 'utf-8'))
    temperature = match[1]
    logger.debug('Reading PI temperature: %s' % temperature)

    mqtt_client.publish("sensors", "cpu_temperature value=%s" % temperature)

  except FileNotFoundError as e:
    logger.error(e)
    pass
