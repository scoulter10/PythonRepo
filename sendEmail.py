import smtplib, ssl

def send_mail():
    content="A Motion has been detected by your monitor - check your log or view your stream now"
    recipient='sarahlouisecoulter5@gmail.com'
    sender='sarahlouisecoulter5@gmail.com'
    mail=smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls() ##transport layer security
    mail.login('sarahlouisecoulter5@gmail.com','gareth94')
    header = 'To:' + recipient + '\n' + 'From: '\
             + sender + '\n' + 'Subject:Motion Detected \n'
    content=header+content
    mail.sendmail(sender,recipient,content)
    mail.close()
    print ("message sent")
