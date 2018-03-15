import os
from ctypes import *
import HCNetSdkTypes
from WebCamCtrl import Position2DirectionPosition
import time
import ctypes.wintypes
from HCNetSdkDefines import HCNetSdkDefines
import keyboard
class HCNetSdk:
    def __init__(self):
        try:
            pwd=os.path.dirname(os.path.abspath(__file__))
            dll_execute = os.path.join(pwd,"./HC/HCNetSDK.dll")  # the directory with the .py file
            dll_current = os.path.join("./HC/HCNetSDK.dll")        # currnet directory
            if not os.path.isfile(dll_execute):
                if not os.path.isfile(dll_current):
                    raise Exception("File not found: %s or %s" % (dll_execute, dll_execute))
                else:
                    self.hsdk = WinDLL(dll_current)  # STEP-1
                    print("dll2 loaded")
            else:
                self.hsdk = WinDLL(dll_execute)  # STEP-1
                print("dll loaded")
        except Exception:
            raise Exception
    def Init(self):
        self.hsdk.NET_DVR_Init()
        self.hsdk.NET_DVR_SetConnectTime(2000, 1)
        self.hsdk.NET_DVR_SetReconnect(10000, True)
    def Login(self,UserName="admin",Password="jishukaifa3432"):
        struLoginInfo = HCNetSdkTypes.NET_DVR_USER_LOGIN_INFO()

        struLoginInfo.bUseAsynLogin = 0
        struLoginInfo.sDeviceAddress = bytes("192.168.1.64", encoding="utf8")
        struLoginInfo.wPort = 8000
        struLoginInfo.sUserName = bytes(UserName, encoding="utf8")
        struLoginInfo.sPassword = bytes(Password, encoding="utf8")

        struDeviceInfoV40 = HCNetSdkTypes.NET_DVR_DEVICEINFO_V40()

        struLoginInfo_p=byref(struLoginInfo)
        struDeviceInfoV40_p=byref(struDeviceInfoV40)

        self.lUserID = c_long(self.hsdk.NET_DVR_Login_V40(struLoginInfo_p,struDeviceInfoV40_p))
        # if(self.GetLastError()!=0):
        #     raise ConnectionError
    def Logout(self):
        self.hsdk.NET_DVR_Logout(self.lUserID)
        self.NET_DVR_Cleanup()
    def PTZControlWithSpeed_Other(self,dwPTZCommand,dwStop,dwSpeed):
        channel_default=1
        self.hsdk.NET_DVR_PTZControlWithSpeed_Other(
            self.lUserID,
            c_long(channel_default),
            ctypes.wintypes.DWORD(dwPTZCommand),
            ctypes.wintypes.DWORD(dwStop),
            ctypes.wintypes.DWORD(dwSpeed))
    def Control(self,command,speed):
        self.PTZControlWithSpeed_Other(command, 0, speed)
    def Halt(self):
        self.PTZControlWithSpeed_Other(27, 1, 7)
    def GetLastError(self):
        print(self.hsdk.NET_DVR_GetLastError())
if __name__=="__main__":
    handle=HCNetSdk()
    handle.Init()
    handle.Login()
    defines = HCNetSdkDefines()
    while(True):
        key = keyboard.read_key()
        if (str(key) == 'KeyboardEvent(down down)'):
            direction, speed = Position2DirectionPosition(320, -240 )

            handle.Control(defines[direction], int(speed))

        if (str(key)=='KeyboardEvent(esc down)'):
            handle.Halt()
    # direction,speed=Position2DirectionPosition(300,10)
    # handle.Control(defines[direction],int(speed))
    # while(True):
    #     key=keyboard.read_key()
    #     print(key)
    #     if (str(key) == 'KeyboardEvent(up down)'):
    #         speed = speed + 1
    #         if (speed > 7):
    #             speed = 7
    #         print(speed)
    #         handle.Control('left', speed)
    #     if (str(key) == 'KeyboardEvent(down down)'):
    #         speed = speed - 1
    #         if (speed < 1):
    #             speed = 1
    #         print(speed)
    #         handle.Control('left', speed)
    #     if (str(key)=='KeyboardEvent(esc down)'):
    #         handle.Halt()
