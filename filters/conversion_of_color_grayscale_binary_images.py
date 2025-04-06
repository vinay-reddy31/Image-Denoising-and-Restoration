import cv2
img=cv2.imread('/content/dog.jpeg')
cv2_imshow(img)
cv2.waitKey(0)
#gray scale
img=cv2.imread ('/content/dog.jpeg',0)
cv2_imshow(img)
cv2.waitKey(0)
#binary image
ret,bw_img=cv2.threshold (img,127,255,cv2.THRESH_BINARY)
cv2_imshow(bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()