import requests
import json
import  time
import random
from readTxt import readTxt
from getPirseId import *
import datetime


class happy:



    def http(url,header1,data):
        respone=requests.post(headers=header1,url=url,data=data)
        return respone

    def http_get(url,header1,data):
        respone=requests.get(headers=header1,url=url,params=data)
        return respone



    def user_login(name, password):
        url="https://appapi.youxiake.com/app/user/login"
        header = {
        "version": "5.0.2",
        "User-Agent": "ios/12.1/iPhone11,8",
        "Authorization": "authorization"
         }
        data={
        "username": name,
        "password": password
    }
        respone=happy.http(url,header,data)
        respones=json.loads(respone.text)
        token = "Bearer " + respones["data"]["token"]
        return token



    def dianzan(id,token):

        url = "https://appapi.youxiake.com/app/discover/prise"
        header = {
        "version": "5.0.2",
            "User-Agent": "ios/12.1/iPhone11,8",
        "Authorization": token,
         }
        data={"quote_id": id}
        respone = happy.http(url, header, data)
        time.sleep(3)
        return respone



    def pinglun(id,token,txt):
        url = "https://appapi.youxiake.com/app/travelarticleComments/add"
        # url="http://192.168.22.172:6002/app/travelarticleComments/add"
        header = {
        "version": "5.0.2",
        "User-Agent": "ios/12.1/iPhone11,8",
        "Authorization": token,
         }
        data={"message": txt,"tid":id}
        respone = happy.http(url, header, data)
        time.sleep(5)
        return respone


    def pinglun2(myNum,token):
        TXT = readTxt.txt(1)
        a = len(TXT) - 1
        requestNum = 0
        id2 = myNum  # 这里减20#
        sum2 = 0
        for i in range(50):
            b = random.randrange(0, a)
            y = happy.pinglun(id2, token, TXT[b])
            requestNum = requestNum + 1
            print(id2,TXT[b],token)
            print(y.text)
            id2 = id2 - 1
            qwe2 = json.loads(y.text)
            if (qwe2["msg"] == "评论成功"):
                sum2 = sum2 + 1
            else:
                sum2 = sum2 + 0
            if sum2 >= 5:
                break
        print("成功", sum2, "个")
        return requestNum



if __name__ == "__main__":
    Token = happy.user_login(17777777777, 123456)
    # Prise_Data = GetID.retrun_Data(Token)
    # sum1=0
    # for i in range(0,50):
    #  x=happy.dianzan(Prise_Data[i],Token)
    #  qwe=json.loads(x.text)
    #  print(qwe)
    #  if(qwe["msg"]=="点赞成功"):
    #      sum1=sum1+1
    #  else:
    #      sum1=sum1+0
    # print("成功",sum1,"个")
    # print(datetime.datetime.now())

    pinglunID=int(readTxt.txt2(1)[0])
    x=happy.pinglun2(pinglunID,Token)
    readTxt.updataTxt(x)







