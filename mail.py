import datetime
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

def send_mail(URL,price,Title,mailid):
    
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login(os.getenv("MAIL_ID"),os.getenv("PASS"))

  subject = 'Eyedropper alert'
  body = "Price of "+Title+" fell below your expected value of "+str(price)+"\n\n"+"click here : "+URL

  msg = f"Subject: {subject}\n\n{body}"
  
  server.sendmail(
    os.getenv("MAIL_ID"),
    mailid,
    msg
  )

  server.quit()