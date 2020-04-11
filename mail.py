import datetime
import smtplib

def send_mail(URL,price,Title,mailid):
    
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('cruxpunch@gmail.com', 'live4Evr')

  subject = 'Eyedropper alert'
  body = "Price of "+Title+" fell below your expected value of "+str(price)+"\n\n"+"click here : "+URL

  msg = f"Subject: {subject}\n\n{body}"
  
  server.sendmail(
    'cruxpunch@gmail.com',
    mailid,
    msg
  )

  server.quit()