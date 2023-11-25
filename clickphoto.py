import cv2

cap = cv2.VideoCapture(0)
status, image1 = cap.read()


photo1 = image1[150:400, 200:450]
photo1_resized = cv2.resize(photo1, (200, 200))


photo1_gray = cv2.cvtColor(photo1_resized, cv2.COLOR_BGR2GRAY)


image1[0:200, 0:200] = cv2.cvtColor(photo1_gray, cv2.COLOR_GRAY2BGR)

cv2.imshow("crop_photo", image1)
cv2.waitKey() == 13

cv2.destroyAllWindows()
cap.release()
