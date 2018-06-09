import cv2
import time
pathin='./data/test10.mp4'
pathout=pathin[:-4]+'/result/'
final2=cv2.imread('./data/test.png',cv2.IMREAD_COLOR)
cv2.imshow("temp",final2)
cv2.waitKey(0)

now = time.localtime()
file_name = pathout+"%04d-%02d-%02d_%02d-%02d-%02d.jpg" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
print(file_name)
print(pathout+file_name)
cv2.imwrite("C:\\Users\\adboy\\Documents\\카카오톡 받은 파일\\test16\\result\\temp222.jpg",final2)  # save frame as JPEG file
