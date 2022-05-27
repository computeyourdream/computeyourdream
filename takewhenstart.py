"""This project takes photo when you start your computer"""
import datetime
import time
import cv2  # kullanacağın modülü içe aktar
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys

camera = cv2.VideoCapture(0)# to use webcam
return_value,image = camera.read()# to read webcam.
yil=datetime.datetime.now()#to take time of now
foto_Isim="Foto_"+str(yil.day)+"_"+str(yil.month)+"_"+str(yil.year)+"_"+str(yil.hour)+"_"+str(yil.minute)+"_"+str(yil.second)
print(foto_Isim)#to convert time variable to string for use name of photo
resim=cv2.imwrite("/home/mustafa/Masaüstü/resimler/"+foto_Isim+".jpg", image)#to save photo
time.sleep(3)
camera.release()
cv2.destroyAllWindows()# Tüm ekranları kapat

# Gmail email sunucusuna bağlanıyoruz
try:

    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("mailadres@xxxxxxx.com", "password")
    mesaj = MIMEMultipart()
    mesaj["From"] = "smailadres@xxxxxxx.com"           # Gönderen
    mesaj["To"]="mailadres@xxxxxxx.com"
    mesaj["Subject"] = "Python Smtp ile Mail Gönderme"    # Konusu
    body = """
    #Python ile smtp ve email modülünü kullanarak mail gönderiyorum.
    
"""+foto_Isim+" Kişisi "+str(yil.day)+"/"+str(yil.month)+"/"+str(yil.year)+" tarihinde Saat: "+str(yil.hour)+":"+str(yil.minute)+":"+str(yil.second)+"' de Oturum Açmıştır."
   #ÖNEMLİİİİİ ______-------  dosya okuma işine bakılacak........
    """eklenecek_Dosya_Ismi=cv2.imread("/home/mustafa/Masaüstü/resimler"+foto_Isim)
    eklenecek_Dosya=open(eklenecek_Dosya_Ismi,'rb')
    print(eklenecek_Dosya_Ismi,"eklenecek")
    yukle=MIMEBase('application','octate-stream')
    yukle.set_payload((eklenecek_Dosya).read())
    encoders.encode_base64(yukle)
    yukle.add_header('Content-Decomposition','attachment', filename=eklenecek_Dosya)
    mesaj.attach(yukle)"""


    body_text = MIMEText(body, "plain")
    mesaj.attach(body_text)
    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    print("Mail başarılı bir şekilde gönderildi.")
    mail.close()

# Eğer mesaj gönderirken hata olursa, hata mesajını konsole yazdırıyorum.
except:
    print("Hata:", sys.exc_info()[0])


