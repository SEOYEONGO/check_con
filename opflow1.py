import sys
import numpy as np
import cv2

src1 = cv2.imread('C:/HH/result/screenshot1.png')
src2 = cv2.imread('C:/HH/result/screenshot68.png')


if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

gray1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)

pt1 = cv2.goodFeaturesToTrack(gray1, 50, 0.01, 10)
pt2, status, err = cv2.calcOpticalFlowPyrLK(src1, src2, pt1, None)

dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)
array=[]
max = 0

for i in range(pt2.shape[0]):
    if status[i, 0] == 0:
        continue

    cv2.circle(dst, tuple(pt1[i, 0].astype(int)), 4, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.circle(dst, tuple(pt2[i, 0].astype(int)), 4, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.arrowedLine(dst, tuple(pt1[i, 0].astype(int)), tuple(pt2[i, 0].astype(int)), (0, 255, 0), 2)
    ar = pt2[i, 0].astype(int) - pt1[i, 0].astype(int)
    # print(abs(ar))
    ar = abs(ar)
    a = ar[:1]
    b = ar[1:]
    # print(a,' ' ,b)
    if max < (a+b):
        max = a+b

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
