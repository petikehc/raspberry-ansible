import paho.mqtt.client as mqtt
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

#  function
def connect_msg():
    logger.info('Connected to Broker')

# function
def publish_msg():
    logger.info('Message Published')

# Creating client
client = mqtt.Client()

# Connecting callback functions
client.on_connect = connect_msg
client.on_publish = publish_msg

# Connect to broker
client.connect("127.0.0.1",1883)