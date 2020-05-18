import subprocess

def read_pi_temperature():

  try:
    cmd = ['/usr/bin/vcgencmd', 'measure_temp']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    stdout,stderr = p.communicate()
    print('Reading PI temperature: %s' % stdout)
  except FileNotFoundError as e:
    print(e)
    pass
