# example path: "/Users/diegorao/Desktop/Drone Stuff/Ball Templates/Red"
import sys
import os
import cv2 as cv
import numpy as np

def main():
    if len(sys.argv) > 1:
        ims = im_list(sys.argv[1])
    else:
        ims = im_list('ims')
    go(ims)

def im_list(source):
    files = os.listdir(source)
    ims = [cv.imread(source + '/' + name) for name in files]
    return ims

def go(ims):
    # set up output image (initially blank) according to average dimensions
    width_out = 0
    height_out = 0
    for im in ims:
        width_out += len(im[0])
        height_out += len(im)
    width_out = int(width_out/len(ims))
    height_out = int(height_out/len(ims))
    out = np.zeros((height_out, width_out, 3), np.uint8)

    # compute average
    ims = [cv.resize(im, (width_out, height_out)) for im in ims]
    for i in range(len(ims)+1)[1:]:
        out = cv.addWeighted(out, (i - 1) / i, ims[i - 1], 1 / i, 0)

    # display output
    cv.imshow('Average Image', out)
    cv.waitKey(0)

    cv.imwrite('output.jpg', out)
if __name__ == '__main__':
    main()