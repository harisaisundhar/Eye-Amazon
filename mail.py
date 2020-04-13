import datetime
import smtplib

def send_mail(URL,price,Title,mailid):
    
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('<gmail_id>', '<gmail_pass>')

  subject = 'Eyedropper alert'
  body = "Price of "+Title+" fell below your expected value of "+str(price)+"\n\n"+"click here : "+URL

  msg = f"Subject: {subject}\n\n{body}"
  
  server.sendmail(
    '<gmail_id>',
    mailid,
    msg
  )

  server.quit()