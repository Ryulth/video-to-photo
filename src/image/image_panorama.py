import argparse
import imutils
import cv2
from panorama import Stitcher
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
imageA = cv2.imread('./data/temp10.jpg',cv2.IMREAD_COLOR)
imageA = cv2.resize(imageA, (0, 0), 1, .25, 0.5)
height, width = imageA.shape[:2]
imageB = cv2.imread('./data/temp30.jpg',cv2.IMREAD_COLOR)
imageB = cv2.resize(imageB, (width, height), 1, .25, 0.5)
# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
(result2,vis2) = stitcher.stitch([imageB, imageA], showMatches=True)
#(result3,vis3) =stitcher.stitch([result2, result], showMatches=True)
# show the images
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint", vis)
cv2.imshow("Result", result)
result2=cv2.resize(result, (0, 0), 1, .25, 0.5)
#cv2.imshow("result2",result2)
#cv2.imshow("Keypoint2", vis2)
#cv2.imshow("Result2", result2)
#cv2.imshow("Keypoint3", vis3)
#cv2.imshow("Result3", result3)

#cv2.imwrite('./image/result.jpg',result)
cv2.waitKey(0)
cv2.destroyAllWindows()