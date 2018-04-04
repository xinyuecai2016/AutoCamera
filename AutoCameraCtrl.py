from HCNetSdk import HCNetSdk
from HCNetSdkDefines import HCNetSdkDefines
from object_detection.Object_detection_video import DroneDetect
import math
import threading
from SLAM import Position2DirectionSpeed
# handle=HCNetSdk()
# handle.Init()
# handle.Login()
# defines = HCNetSdkDefines()
# direction, speed = Position2DirectionPosition(320, -240)
# handle.Halt()
from multiprocessing import Process,Queue

def CoordinateSolve(que_coorddinate,que_cmd):
    detect_counter=0
    normal_counter=0
    x=0
    y=0
    while(not que_coorddinate.empty()):
        coordinate=que_coorddinate.get()
        normal_counter=normal_counter+1.0
        if(coordinate[0]==1):
            detect_counter=detect_counter+1.0
            x = x+coordinate[1]
            y = y+coordinate[2]
            with open('data.text','a') as f:
                f.write(str(x)+' '+str(y)+'\n')
    if(normal_counter!=0 and detect_counter/normal_counter>0.6):
        x=x/detect_counter
        y=y/detect_counter
        print(x,y)
        (cmd,speed)=Position2DirectionSpeed(x,y)
        # print(cmd)
        # print("normal counter" + str(normal_counter))
        # print("detect counter" + str(detect_counter))
        # print("Detected")
        que_cmd.put(cmd+','+speed)

    global timer
    timer=threading.Timer(0.15,CoordinateSolve,[que_coorddinate,que_cmd])
    timer.start()

def CameraCtrl(hcsdk,que_cmd,last_cmd):
    if(not que_cmd.empty()):
        cmd=que_cmd.get()
        if(cmd!=last_cmd):
            t=cmd.split(',')
            hcsdk.ControlBySpeed(t[0],int(t[1]))
            last_cmd=cmd
            print(cmd)
    global timer
    timer=threading.Timer(0.025,CameraCtrl,[hcsdk,que_cmd,last_cmd])
    timer.start()
if __name__ =="__main__":
    handle=HCNetSdk()
    handle.Init()

    handle.Login()
    Data=Queue(100)
    Data_cmds=Queue(100)
    t=Process(target=DroneDetect, args=(Data,))
    CoordinateSolve(Data, Data_cmds)
    CameraCtrl(handle, Data_cmds,'')
    t.start()









