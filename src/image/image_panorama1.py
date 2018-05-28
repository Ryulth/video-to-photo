import argparse
import cv2

'''
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
	help="path to the first image")
ap.add_argument("-s", "--second", required=True,
	help="path to the second image")
args = vars(ap.parse_args())
'''

# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
imageA = cv2.imread('./data/korea_bjj.PNG',cv2.IMREAD_COLOR)
imageB = cv2.imread('./data/korea_bjj_left.png',cv2.IMREAD_COLOR)
imageC = cv2.imread('./data/temp30.jpg',cv2.IMREAD_COLOR)

# stitch the images together to create a panorama
#stitcher = Stitcher()
stitcher = cv2.createStitcher(False)
images=[]
images.append(imageA)
images.append(imageB)
#images.append(imageC)

try :
    result = stitcher.stitch(images)
    cv2.imshow("result", result[1])
except cv2.error:
    print("error for code" , result[0])
    '''error code 
    OK = 0,
    ERR_NEED_MORE_IMGS = 1,
    ERR_HOMOGRAPHY_EST_FAIL = 2,
    ERR_CAMERA_PARAMS_ADJUST_FAIL = 3
    '''
print(stitcher.workScale())
# show the images
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Image C", imageC)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("./data/result.jpg",result[1])

#cv2.imwrite('./image/result.jpg',result)