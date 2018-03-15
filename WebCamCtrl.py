# (x1,y1)---------------------(x2,y1)
#    |                           |
#    |                           |
#    |                           |
#    0------------------------(x2,y2)
# the default size of video frame is 640*480
import math
def Angle2Direction(angle):
    abs_angle=abs(angle)
    direction=round(angle/45)
    return int(math.copysign(direction,angle))
def Position2DirectionPosition(x,y):
    range=math.sqrt(x*x+y*y)    #note that rangle_max=800
    angle = math.atan2(y, x)/math.pi*180
    direction=Angle2Direction(angle)
    speed=math.ceil(range/100)
    if(speed>7):
        speed=7
    if(abs(direction)==2):
        speed=round(speed/480.0*640.0)
    return (direction,speed)
if __name__ =="__main__":
    # lst = [1, 1, 0, 2, 0, 0, 8, 3, 0, 2, 5, 0, 2, 6]
    # lst = [x for x in lst if x != 0]
    # print(lst)
    # TransPosition2Command(1,-1)
    print(Position2DirectionPosition(-10,1))









