import cv2
import numpy as np

img = cv2.imread('./data/korea_bjj.PNG',cv2.IMREAD_COLOR)

cv2.imshow('korea_bjj_show',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

px = img [100,200]# 3번쨰 Array값 중 0번째는 Blue, 1번째는 Green, 2번째는 Red
print (px)


img [100]=[255,255,255]
img [:,100]=[255,255,255]





#for j in img[200] :


cv2.imshow('./image/korea_bjj_show_change',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite('korea_bjj_change.PNG',img)

print(img.shape)
print(img.shape[0])