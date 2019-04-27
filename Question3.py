import os
import sys
import psutil
import time

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

def main():
    if(len(sys.argv)==2):
        processes = getProcList()
        try:    
            CreateLog(sys.argv[1],processes)
        except Exception as eObj:
            print(eObj)
    else:
        print("Incorrect arguments!")

if __name__ == "__main__":
    main()