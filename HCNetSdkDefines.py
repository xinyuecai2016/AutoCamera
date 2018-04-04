import re
import os
def HCNetSdkDefines():
    dll = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./HC/hcnetsdk.h")
    f = open(dll,encoding='utf8')             # 返回一个文件对象
    line = f.readline()       # 调用文件的 readline()方法
    d=dict()
    while line:
        m = re.search('^#define[ ]+([\w\d_]+)[ ]+([\w\d_]+)', line)
        if(m!=None):
            if(m.group(2).isdecimal()):
                d[m.group(1)]=int(m.group(2),10)
            elif(m.group(2).upper().find('0X')!=-1):
                d[m.group(1)] = int(m.group(2), 16)
            else:
                pass
        line = f.readline()
    f.close()
    return d
if __name__=="__main__":
    print(HCNetSdkDefines())