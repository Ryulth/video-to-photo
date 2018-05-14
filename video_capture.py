import sys
import argparse
import timeit
import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*(100/6)))    # 1000->1frame 100->10frame  100/6->60frame
        success,image = vidcap.read()
        #print ('Read a new frame: ', success)
        #cv2.imwrite( pathOut + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
        count = count + 1
    print(count)

""""# if __name__=="__main__":
    print("aba")
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    print(args)
    extractImages(args.pathIn, args.pathOut)
"""

pathin='./image/tempvideo1.mp4'
pathout='./image/result'
start = timeit.default_timer()
extractImages(pathin,pathout)
end = timeit.default_timer()
print(end-start)