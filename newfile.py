import cv2,os

# pika = cv2.imread("Assets/pika.png")
# #print(pika)
# cv2.imshow("bobby",pika)
# #cv2.waitKey(delay=5000)
# cv2.waitKey(0)

# pikagrey = cv2.imread("Assets/pika.png",0)
# #print(pika)
# cv2.imshow("bobby1",pikagrey)
# cv2.waitKey(0)

# cv2.imwrite("bobby.png",pikagrey)

# # There are 3 parameters to read an image - 
# #cv2.IMREAD_COLOR (1) => Specify to load the image in color
# #cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
# #cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged

# path = "/Users/sheikhraquib/Desktop"
# os.chdir(path)
# cv2.imwrite("bobby.png",pikagrey)
# b,g,r = cv2.split(pika)
# cv2.imshow("bobby2",b)
# cv2.waitKey(0)
# cv2.imshow("bobby3",g)
# cv2.waitKey(0)3
# cv2.imshow("bobby4",r)
# cv2.waitKey(0)

opencv = cv2.imread("Assets/opencv.png")
cv2.imshow("bob",opencv)
cv2.waitKey(0)
b,g,r = cv2.split(opencv)
cv2.imshow("bob1",b)
cv2.waitKey(0)
cv2.imshow("bob2",g)
cv2.waitKey(0)
cv2.imshow("bob3",r)
cv2.waitKey(0)
opencv[50,1:50] = [0,0,0]
cv2.imshow("bob4",opencv)
cv2.waitKey(0)
