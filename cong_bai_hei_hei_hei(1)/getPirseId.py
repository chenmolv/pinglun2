#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:fengling
# datetime:2019/10/10 10:24
# filename:getPirseId
# software: PyCharm
from youxiake import *
import json


class GetID:
    def sendHttp(Token,num):

        url="https://appapi.youxiake.com/app/discover/list/stream"
        header = {
        "version": "5.0.2",
        "User-Agent": "ios/12.1/iPhone11,8",
        "Authorization": Token
         }
        Params={"page":num,"type":1}
        respones= happy.http_get(url, header, Params)
        data=json.loads(respones.text)
        return data

    def retrun_Data(Token):

        data = []
        count=0
        num=1
        while count<50:
            respones=GetID.sendHttp(Token, num)
            for i in range(0, 15):
                x = respones["data"]["list"][i]
                if "prised" in x:
                    if x["prised"] == False and x["quoteId"] not in data:
                     if count>=50:
                            break
                     else:
                        data.append(x["quoteId"])
                        count = count+1

                    else:
                        continue
            num=num+1
        return data


