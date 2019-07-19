import requests 
import smtplib
from bs4 import BeautifulSoup
URL = 'https://www.amazon.in/Rs-Components-Raspberry-Pi-Motherboard/dp/B07BFH96M3/ref=dp_ob_title_ce'

headers = {"Users-Agent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}
def check_price():

    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    #print(soup.prettify())
    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    converted_price1 = price[2]
    converted_price2 = price[4:7]
    converted_price = converted_price1 + converted_price2
    if(float(converted_price) < float(3500)): send_mail()
    
    
    #print(converted_price)
    #print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('nivas65536@gmail.com','ehwhzuwoswwgbrjq')
    subject = 'Price fell down!'
    body = 'Check the Amazon link:  https://www.amazon.in/Rs-Components-Raspberry-Pi-Motherboard/dp/B07BFH96M3/ref=dp_ob_title_ce'
    
    msg = "Subject: {}\n\n {} ".format(subject ,body)
    server.sendmail(
        'nivas65536@gmail.com',
        '120015097@sastra.ac.in',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')
    server.quit()
check_price()


