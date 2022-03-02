import Adafruit_DHT as AD#Adafruit_DHT 温湿度识别库 需另装
import time
DHT = AD.DHT11#加载地址

for i in range(10):
    hum，temp = AD.read_retry(DHT,26)#26:BCM编码 为GPIO.25
    print(hum,temp)
    time.sleep(1)
