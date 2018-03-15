import cv2
# 主码流码流，观看视频流，高清晰度，高延迟
cap1 = cv2.VideoCapture("rtsp://admin:jishukaifa3432"+
"@192.168.1.64:554/Streaming/Channels/101")
# 第二码流，控制视频流，低延迟，低分辨率
cap2 = cv2.VideoCapture("rtsp://admin:jishukaifa3432"
"@192.168.1.64:554/Streaming/Channels/102?transportmode=unicast")
# 第三码流，我从来没有链接上
cap3 = cv2.VideoCapture("rtsp://admin:jishukaifa3432"
"@192.168.1.64:554/Streaming/Channels/103?transportmode=unicast")
cap=cap1
print(cap.isOpened())

while (cap.isOpened()):
    ret,frame = cap.read()
    cv2.imshow("frame",frame)
    cv2.waitKey(1)