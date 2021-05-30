import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# environment variables
username='mail@gmail.com'
password=''

def send_mail(text='Email Body',subject='hello world',from_email='fathima<mail@gmail.com>',to_emails=None):
    assert isinstance(to_emails,list)
    msg=MIMEMultipart('alternative')
    msg['From']=from_email
    msg['To']=",".join(to_emails)
    msg['Subject']=subject
    txt_part=MIMEText(text,'plain')
    msg.attach(txt_part) 

    html_part=MIMEText("<h1>hi welcom</h1>",'html')
    msg.attach(html_part)

    msg_str=msg.as_string()
    # login to smtp server
    server=smtplib.SMTP(host='smtp.gmail.com',
    port=587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email,to_emails,msg_str)
    server.quit()
    # with smtplib.SMTP() as server:
    #    server.login()
    #    pass
send_mail(to_emails = ['nazmiyaas@gmail.com'])