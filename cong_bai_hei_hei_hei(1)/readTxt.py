import json
class readTxt:

    def txt(self):
        x=open(r"../cong_bai_hei_hei_hei(1)/pinglun.txt","r",encoding='utf-8')
        data=x.readlines()
        return  data

    def clearTxt(self):
        f = open(r"../cong_bai_hei_hei_hei(1)/1.txt", "r+")
        f.truncate()

    def writeTxt(msg):
        f = open(r"../cong_bai_hei_hei_hei(1)/1.txt", "r+")
        f.write(msg)

    def txt2(self):
        x=open(r"../cong_bai_hei_hei_hei(1)/1.txt","r")
        data=x.readlines()
        return  data

    def updataTxt(num):
        txtNum = int(readTxt.txt2(1)[0])
        No=txtNum-num
        readTxt.clearTxt(1)
        readTxt.writeTxt(str(No))

