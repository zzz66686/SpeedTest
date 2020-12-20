# -*- coding: utf-8 -*-
import requests
import time
import threading


TIMES = 3
DEBUG = 0

def debugPrint(s):
    if DEBUG:
        print(s)

def reqBaidu(times = 1,p = None):
    if p == None:
        for i in range(times):
            try:
                res = requests.get('https://www.baidu.com', timeout = 2)
            except Exception as e:
                print(e)
                time.sleep(1)
    else:
        for i in range(times):
            try:
                res = requests.get('https://www.baidu.com', proxies = p, timeout = 2)
            except:
                time.sleep(1)                


def reqTaobao(times = 1,p = None):
    if p == None:
        for i in range(times):
            try:
                res = requests.get('https://www.taobao.com', timeout = 2)
            except:
                time.sleep(1)                    
    else:
        for i in range(times):
            try:
                res = requests.get('https://www.taobao.com', proxies = p, timeout = 2)
            except Exception as e:
                print(e)
                time.sleep(1)                    


def reqQq(times = 1,p = None):
    if p == None:
        for i in range(times):
            try:
                res = requests.get('https://www.qq.com', timeout = 2)
            except:
                time.sleep(1)                    
    else:
        for i in range(times):
            try:
                res = requests.get('https://www.qq.com', proxies = p, timeout = 2)
            except Exception as e:
                print(e)
                time.sleep(1)                    


def test(times = 1, p = None):
    startTime = int(time.time() * 1000)
    reqBaidu(times, p)
    endTime = int(time.time() * 1000)
    duringTime = endTime - startTime
    reqBaiduTime = duringTime/times
    debugPrint('%s: Baidu:%fms.' % (p, reqBaiduTime))
    
    startTime = int(time.time() * 1000)
    reqTaobao(times)
    endTime = int(time.time() * 1000)
    duringTime = endTime - startTime
    reqTaobaoTime = duringTime/times
    debugPrint('%s: Taobao:%fms.' % (p, reqTaobaoTime))
    
    startTime = int(time.time() * 1000)
    reqQq(times)
    endTime = int(time.time() * 1000)
    duringTime = endTime - startTime
    reqQqTime = duringTime/times    
    debugPrint('%s: Qq:%fms.' % (p, reqQqTime))
    
    averageTime = (reqBaiduTime + reqTaobaoTime + reqQqTime) / 3
    print('%s: Baidu:%fms,  Taobao:%fms,  Qq:%fms,  average:%fms.' % (p, reqBaiduTime, reqTaobaoTime, reqQqTime, averageTime))


#test(TIMES)

with open('proxy.txt', 'r') as f:
    proxyList = f.readlines()

threads = []
for p in proxyList:
    p = p.strip()
    proxies = {
    'http':p,
    }
    
    t=threading.Thread(target=test,args=(TIMES,proxies))
    t.start()
    threads.append(t)

