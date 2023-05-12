from machine import Pin, ADC
import network
import socket
from time import sleep
from machine import Pin, ADC

ssid = 'dlink-9D20'
password = 'agmem94986'

adc = ADC(Pin(26, mode=Pin.IN))
adc1=adc.read_u16()

def webpage(voc):
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <p>VOC:{voc} counts</p>
            </body>
            </html>
            """
    return str(html)

v=str(adc1)
html=webpage(v)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    pass

print('IP:', wlan.ifconfig()[0]) # 顯示IP位址

# 建立socket連線物件，繫結到埠口80。
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

# 偵聽用戶端連線請求
while True:
    try:
        #------------------
        #sleep(1)
        adc = ADC(Pin(26, mode=Pin.IN))
        adc1=adc.read_u16()
        v=str(adc1)
        html=webpage(v)
        #------------------
        client, addr = s.accept()
        print('client connected, IP: ', addr)
        client.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        client.send(html)
        client.close()

    except OSError as e:  # 若出現錯誤，則中斷連線。
        client.close()
        print('connection closed')
