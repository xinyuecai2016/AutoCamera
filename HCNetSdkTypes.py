from ctypes import *
from ctypes import wintypes
class LPNET_DVR_DEVICEINFO_V30(Structure):
    SERIALNO_LEN=48
    _fields_ = [('sSerialNumber', c_ubyte*SERIALNO_LEN ),
                ('byAlarmInPortNum', c_ubyte ),
                ('byAlarmOutPortNum', c_ubyte ),
                ('byDiskNum', c_ubyte ),
                ('byDVRType', c_ubyte ),
                ('byChanNum', c_ubyte ),
                ('byStartChan', c_ubyte ),
                ('byAudioChanNum', c_ubyte ),
                ('byZeroChanNum', c_ubyte ),
                ('byMainProto', c_ubyte ),
                ('bySubProto', c_ubyte ),
                ('bySupport', c_ubyte ),
                ('bySupport1', c_ubyte ),
                ('bySupport2', c_ubyte ),
                ('wDevType', c_ushort ),
                ('bySupport3', c_ubyte ),
                ('byMultiStreamProto', c_ubyte ),
                ('byStartDChan', c_ubyte ),
                ('byStartDTalkChan', c_ubyte ),
                ('byHighDChanNum', c_ubyte ),
                ('bySupport4', c_ubyte ),
                ('byLanguageType', c_ubyte ),
                ('byVoiceInChanNum', c_ubyte ),
                ('byStartVoiceInChanNo', c_ubyte ),
                ('bySupport5', c_ubyte ),
                ('bySupport6', c_ubyte ),
                ('byMirrorChanNum', c_ubyte ),
                ('wStartMirrorChanNo', c_ushort ),
                ('bySupport7', c_ubyte ),
                ('byRes2', c_ubyte )]

class NET_DVR_DEVICEINFO_V40(Structure):
    _fields_ = [('struDeviceV30', LPNET_DVR_DEVICEINFO_V30),
                ('bySupportLock', c_ubyte),
                ('byRetryLoginTime', c_ubyte),
                ('byPasswordLevel', c_ubyte),
                ('byProxyType', c_ubyte),
                ('dwSurplusLockTime', c_ushort),
                ('byCharEncodeType', c_ubyte),
                ('bySupportDev5', c_ubyte),
                ('byRes2', c_ubyte*254)]


class NET_DVR_USER_LOGIN_INFO(Structure):
    NET_DVR_DEV_ADDRESS_MAX_LEN = 129
    NET_DVR_LOGIN_USERNAME_MAX_LEN = 64
    NET_DVR_LOGIN_PASSWD_MAX_LEN = 64
    _fields_=[  ('sDeviceAddress',c_char*NET_DVR_DEV_ADDRESS_MAX_LEN),
                ('byUseTransport',c_ubyte),
                ('wPort',c_ushort),#WORD
                ('sUserName',c_char*NET_DVR_LOGIN_USERNAME_MAX_LEN),
                ('sPassword',c_char*NET_DVR_LOGIN_PASSWD_MAX_LEN),
                ('cbLoginResult',CFUNCTYPE(c_voidp, c_long,c_wchar)),
                ('pUser',c_void_p),
                ('bUseAsynLogin',c_bool),
                ('byProxyType',c_ubyte),#BYTE
                ('byUseUTCTime',c_ubyte),
                ('byRes2',c_ubyte*2),
                ('iProxyID',c_long),
                ('byRes3',c_ubyte*120)
                ]

class NET_DVR_PTZ_3D_SPEED_CONTROL(Structure):
    _fields_ = [('dwSize', wintypes.DWORD),
                ('dwChannel',wintypes.DWORD),
                ('byPSpeed',wintypes.BYTE),
                ('byTSpeed',wintypes.BYTE),
                ('byZSpeed',wintypes.BYTE),
                ('byPDirect',wintypes.BYTE),
                ('byTDirect',wintypes.BYTE),
                ('byZDirect',wintypes.BYTE),
                ('byRes',wintypes.BYTE*18),]