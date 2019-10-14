import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://www.amazon.in/Affix-Super-Tough-Fabric-Braided/dp/B07L3NRVDS/ref=lp_16374619031_1_1_sspa?s=electronics&ie=UTF8&qid=1570455747&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExV0xCTU9HOFpaV1NRJmVuY3J5cHRlZElkPUEwODY0NzQ3V1E5RzQ1S1JQRko4JmVuY3J5cHRlZEFkSWQ9QTAyNDk5NDYyN1o2MTNCSlNUSThSJndpZGdldE5hbWU9c3BfYXRmX2Jyb3dzZSZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_saleprice").get_text()
    price = float(price[2:])

    print(title.strip(), price)
    if(price < 200):
        send_email()


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('alcom.mmt@gmail.com', 'nozmtpwwroptqkxn')

    subject = 'price fell down'
    body = 'check the amazon https://www.amazon.in/Affix-Super-Tough-Fabric-Braided/dp/B07L3NRVDS/ref=lp_16374619031_1_1_sspa?s=electronics&ie=UTF8&qid=1570455747&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExV0xCTU9HOFpaV1NRJmVuY3J5cHRlZElkPUEwODY0NzQ3V1E5RzQ1S1JQRko4JmVuY3J5cHRlZEFkSWQ9QTAyNDk5NDYyN1o2MTNCSlNUSThSJndpZGdldE5hbWU9c3BfYXRmX2Jyb3dzZSZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'alcom.mmt@gmail.com',
        'striker.aryu56@gmail.com',
        msg
    )
    print("email has been sent")


check_price()
