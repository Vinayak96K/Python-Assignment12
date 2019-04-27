import os
import sys
import psutil


def getProcList():
    procList = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            procList.append(pinfo)
        except Exception as eObj:
            print(eObj)
    return procList


def main():
    processes = getProcList()
    for proc in processes:
        print(proc)   

if __name__ == "__main__":
    main()