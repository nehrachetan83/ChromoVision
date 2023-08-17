from sys import argv
import cv2

path = "./TestData/"+argv[1]+".jpg"
path_d = "./TestData/"+argv[1]+"_d.jpg"

img = cv2.imread(path)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image",img)
cv2.imshow("Gray Image",gray_image)

cv2.imwrite(path_d,gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()