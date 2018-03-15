# (x1,y1)---------------------(x2,y1)
#    |                           |
#    |             o             |
#    |                           |
#    |------------------------(x2,y2)
# the default size of video frame is 640*480
import math
def Angle2Direction(angle):
    abs_angle=abs(angle)
    direction=round(angle/45)
    return int(math.copysign(direction,angle))
def Direct2Command(direction):
    TranlateTable={
        -3:'UP_LEFT',
        -2:'TILT_UP',
        -1:'UP_RIGHT',
        0:'PAN_RIGHT',
        1:'DOWN_RIGHT',
        2:'TILT_DOWN',
        3:'DOWN_LEFT',
        4:'PAN_LEFT',
    }
    return TranlateTable[direction]
def Position2DirectionPosition(x,y):
    range=math.sqrt(x*x+y*y)    #note that rangle_max=800
    angle = math.atan2(y, x)/math.pi*180
    direction=Angle2Direction(angle)
    speed=math.ceil(range/50)
    if(speed>7):
        speed=7
    if(abs(direction)==2):
        speed=round(speed/480.0*640.0)

    return Direct2Command(direction),str(speed)

if __name__ =="__main__":
    # lst = [1, 1, 0, 2, 0, 0, 8, 3, 0, 2, 5, 0, 2, 6]
    # lst = [x for x in lst if x != 0]
    # print(lst)
    # TransPosition2Command(1,-1)
    # print(Position2DirectionPosition(-10,1))

    print(Direct2Command(-1))








