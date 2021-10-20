# -*- coding: utf-8 -*-
"""
 PYTHON PROGRAMLAMA UYGULAMA ÇALIŞMASI:
 
 Python ile e-mail gönderme uygulaması..
 
 DİKKAT !!!:
     
 Google'ın SMTP server'ları üzerinden mail gönderecekseniz aşağıdaki linkteki google ayarlardan
 mail hesabınıza Google dışından erişime izin vermeniz gerekmektedir. 
 
 https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OGCFLb7S_q2dQmavz6wlUCBzkAB9urEO2jJ74BhiAm5tB1tRCsXABtyF37OAN2XgMaKFxhAhb7_CQO_BGqOoK17Qriww
"""

# secure connection oluşturmak için ya `SMTP_SSL()` portno:465 veya `.starttls()` port no:587 kullanılabilir.
# SMTP_SSL() progrmaın başlangıcında güvenli bir bağlantı oluşturur. 
# starttls ise başlangıçta güvensiz olana ancak sizin `.starttls()` çağırmanızla güvenli hale gelen bir bağlantı oluşturur..

import smtplib
from email.mime.text import MIMEText


try: 
    #Create your SMTP session 
    smtp = smtplib.SMTP('smtp.gmail.com', 587) 

    #Use TLS to add security  
    smtp.starttls() 

    #User Authentication     
    smtp.login("sender_email_id","sender_email_id_password")    
   
    
    #Defining The Message 
    mesaj = "Merhaba, bu bir Python test çalışmasıdır.."    
    msg = MIMEText(mesaj.encode('utf-8'), _charset='utf-8')
    
    #Sending the Email
    smtp.sendmail("test@gmail.com", "test@gmail.com", msg.as_string()) 
    #smtp.sendmail("sender_email_id", "receiver_email_id", message) 

    #Terminating the session 
    smtp.quit() 
    print ("Email başarıyla gönderildi !!") 

except Exception as ex: 
    print("Birşeyler ters gitti email gönderilemedi...", ex) 
    

