import cv2
import time
pathin='./data/test10.mp4'
pathout=pathin[:-4]+'/result/'
final=cv2.imread('./data/test10.jpg',cv2.IMREAD_COLOR)
cv2.imshow("temp",final)
cv2.waitKey(0)
now = time.localtime()
save_file = pathout+"\\%04d-%02d-%02d-%02d:%02d:%02d.jpg" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
print(save_file)
cv2.imwrite("./data/test10.jpg",final)  # save frame as JPEG file