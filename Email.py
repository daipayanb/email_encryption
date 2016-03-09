import ast
import smtplib
from RSA import rsakeygen
from RSA import aeskeygen
from RSA import rencrypt
from RSA import rdecrypt
from Crypto.PublicKey import RSA

def newuser(email):
    rsakeygen(email)

def encrypt_email(sender,receivers,subject,message1,password):
    key=None
    pubkey=None
    aeskey=None

    for receiver in receivers:
        message=message1
        f=open(receiver+'.pem','r')
        key=RSA.importKey(f.read())
        pubkey=key.publickey()
        f.close()

        aeskey=aeskeygen()
        subject1=str(pubkey.encrypt(aeskey,32))
        subject=rencrypt(subject,aeskey)
        message=rencrypt(message,aeskey)+"#########################AESKEY#########################"+subject1

        message = """\
   From: %s
To: %s
Subject: %s

%s
""" % (sender, ", ".join(receiver), subject1, message)



        email=sender.split('@')
        if email[1]=='gmail.com':

            try:
                session = smtplib.SMTP('smtp.gmail.com',587)
                session.ehlo()
                session.starttls()
                session.ehlo()
                session.login(sender,password)
                session.sendmail(sender,receiver,message)
                session.quit()
                print ("Message sent successfully.")
            except smtplib.SMTPException:
                print ('Error')

        if email[1]=='yahoo.com':
            try :
                server = smtplib.SMTP("smtp.mail.yahoo.com",25)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(sender,password)
                server.sendmail(sender,receiver,message)
                server.quit()
                print ('Message sent successfully.')
            except smtplib.SMTPException:
                print ('Error')
            

        if email[1]=='live.com':
            try :
                s = smtplib.SMTP("smtp.live.com",587)
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(sender,password)
                s.sendmail(sender,receiver,message)
                s.quit()
                print ('Message sent successfully.')
            except smtplib.SMTPException:
                print ('Error')

        if email[1]=='office365.com':
            try :
                s = smtplib.SMTP("smtp.office365.com",587)
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(sender,password)
                s.sendmail(sender,receiver,message)
                s.quit()
                print ('Message sent successfully.')
            except smtplib.SMTPException:
                print ('Error')

        if email[1]=='rediffmail.com':
            try :
                s = smtplib.SMTP("smtp.rediffmail.com",587)
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(sender,password)
                s.sendmail(sender,receiver,message)
                s.quit()
                print ('Message sent successfully.')
            except smtplib.SMTPException:
                print ('Error')

        if email[1]=='aol.com':
            try :
                s = smtplib.SMTP("smtp.aol.com",587)
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(sender,password)
                s.sendmail(sender,receiver,message)
                s.quit()
                print ('Message sent successfully.')
            except smtplib.SMTPException:
                print ('Error')

        if email[1]=='msn.com':
            try :
                s = smtplib.SMTP("smtp.email.msn.com",587)
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(sender,password)
                s.sendmail(sender,receiver,message)
                s.quit()
                print ('Message sent successfully.')
            except smtplib.SMTPException:
                print ('Error')

def decrypt_email(email,message):
    #email=raw_input("Your email id? ")
    '''f=open(email+'.txt','r')
    cipher=f.read()
    f.close()'''
    cipher=message.split("#########################AESKEY#########################")
    #f=open(email+'subject.txt','r')
    aeskey=ast.literal_eval(str(cipher[1]))
    #f.close()
    f=open(email+'.pem','r')
    key=RSA.importKey(f.read())
    f.close()
    aeskey=key.decrypt(aeskey)
    plaintext=rdecrypt(cipher[0],aeskey)
    return plaintext



'''while(True):
    choice=raw_input("*****MENU*****\n 1. Send Encrypted Mail \n 2. Decrypt Mail \n 3. Exit \n Enter Choice: \n")
    if choice=='1':
        encrypt_email()
    elif choice=='2':
        decrypt_email()
    elif choice=='3':
        exit(0)'''






