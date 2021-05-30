import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

form template import Template
# environment variables
username='mail@gmail.com'
password=''

class Emailer():
    subject="hello world"
    to_emails=[]
    has_html=False
    test_send=False
    from_email='fathima<mail@gmail.com>'
    def __init__(self,subject="",template_name=None,context={},template_html=None,to_emails=None,test_send=False):
        if template_name==None and template_name==None:
            raise Exception("you must set a template")
        assert isinstance(to_emails,list)
        self.to_emails=to_emails
        self.subject=subject
        if template_html!=None:
            self.has_html=True
            self.template_html=template_html
        self.template_name=template_name
        self.test_send=test_send
    def format_msg(self):

    def send_mail(self):
        msg=MIMEMultipart('alternative')
        msg['From']=from_email
        msg['To']=",".join(to_emails)
        msg['Subject']=subject
        txt_part=MIMEText(text,'plain')
        msg.attach(txt_part) 
        if html!=None:
            html_part=

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