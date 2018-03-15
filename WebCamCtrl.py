import os
import ctypes, ctypes.wintypes
import HCNetSdkTypes
import time
try:
    dll = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./HC/HCNetSDK.dll") # the directory with the .py file
    dll2 = os.path.join("./HC/HCNetSDK.dll") # currnet directory
    if not os.path.isfile(dll):
        if not os.path.isfile(dll2):
            raise Exception("File not found: %s or %s" % (dll,dll2))
        else:
            hsdk = ctypes.WinDLL(dll2) # STEP-1
            print("dll2 loaded")
    else:
        hsdk = ctypes.WinDLL(dll) # STEP-1
        print("dll loaded")
        hsdk.NET_DVR_Init()
        hsdk.NET_DVR_SetConnectTime(2000, 1)
        hsdk.NET_DVR_SetReconnect(10000, True)
        struLoginInfo = HCNetSdkTypes.NET_DVR_USER_LOGIN_INFO()
        struLoginInfo.bUseAsynLogin = 0
        struLoginInfo.sDeviceAddress = bytes("192.168.1.64",encoding="utf8")
        struLoginInfo.wPort = 8000
        struLoginInfo.sUserName = bytes("admin",encoding="utf8")
        struLoginInfo.sPassword = bytes("jishukaifa3432",encoding="utf8")
        struDeviceInfoV40 = HCNetSdkTypes.NET_DVR_DEVICEINFO_V40()



        lUserID=ctypes.c_long(hsdk.NET_DVR_Login_V40(ctypes.byref(struLoginInfo), ctypes.byref(struDeviceInfoV40)))

        hsdk.NET_DVR_PTZControlWithSpeed_Other(lUserID,ctypes.c_long(1), ctypes.wintypes.DWORD(27),
                                               ctypes.wintypes.DWORD(0),ctypes.wintypes.DWORD(7))
        time.sleep(1)
        hsdk.NET_DVR_PTZControlWithSpeed_Other(lUserID, ctypes.c_long(1), ctypes.wintypes.DWORD(27),
                                               ctypes.wintypes.DWORD(1), ctypes.wintypes.DWORD(7))
        hsdk.NET_DVR_Logout(lUserID)
        hsdk.NET_DVR_Cleanup()
        print(hsdk.NET_DVR_GetLastError())




except Exception:
    raise Exception
# version = "%.8x" % hsdk.PlayM4_GetSdkVersion()
# print (version, " <- PlayM4_GetSdkVersion()")







