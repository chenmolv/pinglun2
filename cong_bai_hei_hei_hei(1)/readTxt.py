import json
import  os
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.dirname(current_dir)+'\\'+"cong_bai_hei_hei_hei(1)"+'\\'
pathTravleId = parent_path + '\\' + 'TravelID.txt'
class readTxt:

    def txt(path):
        x=open(path,"r",encoding='utf-8')
        data=x.readlines()
        return  data

    def clearTxt(path):
        f = open(path, "r+")
        f.truncate()

    def writeTxt(path,msg):
        f = open(path, "r+")
        f.write(msg)


    def updataTxt(path,num):
        txtNum = int(readTxt.txt(path)[0])
        No=txtNum-num
        readTxt.clearTxt(path)
        readTxt.writeTxt(path,str(No))


