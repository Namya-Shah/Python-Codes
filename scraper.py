import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Verilux%C2%AE-Charging-Ethernet-MacBook-Enabled/dp/B09TDRQ7F5/ref=sr_1_3?keywords=usb+c+hub+macbook+air+m1&qid=1655231280&sprefix=usb+c+hub+mac%2Caps%2C196&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36' }

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price > 1.000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('namya.shah123@gmail.com', 'neelnamya1')
    
    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/Verilux%C2%AE-Charging-Ethernet-MacBook-Enabled/dp/B09TDRQ7F5/ref=sr_1_3?keywords=usb+c+hub+macbook+air+m1&qid=1655231280&sprefix=usb+c+hub+mac%2Caps%2C196&sr=8-3'
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'namya.shah123@gmail.com',
        msg
    )
    print('Hey Email has been sent!')
    
    server.quit()
    
    
check_price()