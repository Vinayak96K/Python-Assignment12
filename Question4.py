import os
import sys
import psutil
import time
import smtplib
import urllib2
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_Connected():
    try:
        urllib2.urlopen('http://216.58.192.142',timeout=1)
        return True
    except urllib2.URLError as eObj:
        return False

def SendMail(strLog,strMailTo):
    try:
        strfrom ="vinayak.patil0304@gmail.com"
        msg = MIMEMultipart()
        msg['From']=strfrom
        msg['To']=strMailTo
        body = """
        Hello %s,
        Please find attached document which contains log of Running proccesses...
        This is an auto genrated message.
        Thank you,
        Vinayak Mahendra Patil.
        """%(strMailTo)
        Subject='Marvellous process logger'
        msg['Subject']=Subject
        msg.attach(MIMEText(body,'plain'))
        attachment = open(strLog,'rb')
        p = MIMEBase('application','octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition','attachment;filename=%s'%(strLog))
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(strfrom,'----------------')
        text = msg.as_string()
        s.sendmail(strfrom,strMailTo,text)
        s.quit()
        print('Log file successfully sent through mail!')

    except Exception as eObj:
        print(eObj)


def getProcList():
    procList = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            procList.append(pinfo)
        except Exception as eObj:
            print(eObj)
    return procList

def CreateLog(sDirPath,ProcList):
    if not os.path.isabs(sDirPath):
        sDirPath = os.path.abspath(sDirPath)
    if not os.path.exists(sDirPath):
        os.mkdir(sDirPath)
    
    filePath= os.path.join(sDirPath,"ProcessInfo_%s.log"%(time.ctime()))
    fd = open(filePath,'w')
    strHeader = '-' * 80
    fd.write(strHeader+"\n\t\t\t"+"Marvellous Process Logger\t\n"+strHeader+"\n\n")
    for proc in  ProcList:
        fd.write("%s\n"%(proc))
    fd.close()
    return filePath

def main():
    if(len(sys.argv)==3):
        processes = getProcList()
        try:    
            logfile = CreateLog(sys.argv[1],processes)
            if(is_Connected()):
                SendMail(logfile,sys.argv[2])
            else:
                print('No Internet access...\nPlease connect to internet!')
        except Exception as eObj:
            print(eObj)
    else:
        print("Incorrect arguments!")

if __name__ == "__main__":
    main()