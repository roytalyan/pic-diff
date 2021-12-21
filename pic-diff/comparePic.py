#from skimage.measure import compare_ssim
#~ import skimage as ssim
from skimage.metrics import structural_similarity   # pip install scikit-image
import argparse
import imutils
import cv2

# imageA = cv2.imread("3.png")
# imageB = cv2.imread("4.png")


def cut(image):
    y = 0
    h = image.shape[0]
    x = 150
    w = 850
    return image[y:y + h, x:x + w]
    crop = image[y:y + h, x:x + w]
    cv2.imshow('Image', crop)
    cv2.waitKey(0)


imageA = cv2.imread("master.png")   # (588, 1172, 3)
imageB = cv2.imread("remote.png")   #
imageA = cut(imageA)

print(imageA.shape)
print(imageB.shape)
imageA = cv2.resize(imageA, (imageB.shape[1], imageB.shape[0]))
# imageB = cv2.resize(imageB, (imageA.shape[1], imageA.shape[0]))
cv2.imshow("Modified", imageA)
cv2.waitKey(0)

print(imageA.shape)
print(imageB.shape)

grayA = cv2.cvtColor(imageA,cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB,cv2.COLOR_BGR2GRAY)


(score,diff) = structural_similarity(grayA,grayB,full = True)
diff = (diff *255).astype("uint8")
print("SSIM:{}".format(score))

thresh = cv2.threshold(diff,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#cnts = cnts[0] if imutils.is_cv2() else cnts[1]
cnts = imutils.grab_contours(cnts)

for c in cnts:
 (x,y,w,h) = cv2.boundingRect(c)
 cv2.rectangle(imageA,(x,y),(x+w,y+h),(0,0,255),2)
 cv2.rectangle(imageB,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow("Modified",imageB)
cv2.imwrite("diff2.png",imageB)
cv2.waitKey(0)