import os
import sys
import psutil


def getProcInfo(sProc):
    procList = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            if(pinfo.get('name') == sProc):
                print(pinfo)
        except Exception as eObj:
            print(eObj)
    return procList

def main():
    if(len(sys.argv)==2):
        processes = getProcInfo(str(sys.argv[1]))
    else:
        print('Specify the process name!')

if __name__ == "__main__":
    main()