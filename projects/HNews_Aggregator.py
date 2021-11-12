import requests
from bs4 import BeautifulSoup
#Send the mail
import smtplib
#email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#system date and time manipulation
import datetime
now = datetime.datetime.now()

#email content placeholder
content = ''

#extracting Hacker News Stories
def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+' :: '+tag.text + "\n" + '<br>') if tag.text != 'More' else '')
        #print(tag.prettify) #find all('span', attrs={'class':'sitestr'}))
    return(cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message')

#lets send the mail
print('Composing Email...')

#update your email details
SERVER = 'smtp.gmail.com' #"Your smtp server"
PORT = 587 #your port number
FROM = 'neelshah725@gmail.com' #your email id
TO = 'neelshah725@gmail.com' #your second email id #it can be a list
PASS = 'ayushineel1'

#fp = open(file_name, 'rb')
#Create a text/plain message
#msg = MIMEText('')
msg = MIMEMultipart()

#msg.add_header('Content-Disposition', 'attachment', 'filename='empty.txt')
msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg["To"] = TO

msg.attach(MIMEText(content, 'html'))
#fp.close()

print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()