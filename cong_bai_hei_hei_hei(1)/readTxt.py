import json
import  os
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.dirname(current_dir)+'\\'+"cong_bai_hei_hei_hei(1)"+'\\'
path1 = parent_path + '\\' + '1.txt'
pathPinglun=parent_path + '\\' + 'pinglun.txt'
class readTxt:

    def txt(self):
        x=open(pathPinglun,"r",encoding='utf-8')
        data=x.readlines()
        return  data

    def clearTxt(self):
        f = open(path1, "r+")
        f.truncate()

    def writeTxt(msg):
        f = open(path1, "r+")
        f.write(msg)

    def txt2(self):
        x=open(path1,"r",encoding='utf-8')
        data=x.readlines()
        return  data

    def updataTxt(num):
        txtNum = int(readTxt.txt2(1)[0])
        No=txtNum-num
        readTxt.clearTxt(1)
        readTxt.writeTxt(str(No))

