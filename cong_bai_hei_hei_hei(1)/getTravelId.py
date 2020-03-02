from youxiake import *


class Travel:
    def getList(ToKen,Page):
        params = []
        URL="https://appapi.youxiake.com/app/travelarticles/digestList"
        header = {
        "version": "5.0.2",
        "User-Agent": "ios/12.1/iPhone11,8",
        "Authorization": ToKen
         }
        Params = {"curPage": Page}
        respones = happy.http_get(URL, header, Params)
        data = json.loads(respones.text)
        for i in range(0,19):
         params.append([data["data"]["list"][i]["tid"],data["data"]["list"][i]["replies"]])
        return params



    def getComment(Token,page,ID):
        URL="https://appapi.youxiake.com/app/travelarticles/digestList"
        header = {
        "version": "5.0.2",
        "Authorization": Token,
        "User-Agent":"ios/12.1/iPhone11,8"
         }
        Params = {"curPage": page,"tid":ID}
        respones = happy.http_get(URL, header, Params)
        data = json.loads(respones.text)
        return data


    def getCommentID(totelRepiles,comment):
        data=[]
        for i in range (totelRepiles):
            data.append(comment["data"]["list"][i]["authorid"])
            return data



    def isComment(Token):
        data=[]
        listPage=1
        while len(data)<20:
            list=Travel.getList(Token,listPage)
            for i  in range(16):
                totelRepiles=int(list[i][1])
                ID=list[i][0]
                page=totelRepiles/15
                count=int(page)
                if(count<=1):
                    comment = Travel.getComment(Token,1,ID)
                    commentID=Travel.getCommentID(totelRepiles,comment)
                    if "10865152" in commentID:
                     continue
                    else:
                     if len(data)>20:
                         break
                     else:
                        data.append(ID)
                else:
                 for i in  range(1,count+2):
                    comment = Travel.getComment(Token,i,ID)
                    commentID=Travel.getCommentID(totelRepiles,comment)
                 if "10865152" in commentID:
                     continue
                 else:
                    if len(data) > 20:
                         break
                    else:
                        data.append(ID)
            listPage=listPage+1
        return  data




