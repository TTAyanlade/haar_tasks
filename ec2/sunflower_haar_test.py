import cv2
import os


cascade = cv2.CascadeClassifier("sunflower.xml")


img = cv2.imread("test_image/test1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


objects = cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=10,
    minSize=(400, 400)
)

for (x, y, w, h) in objects:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


output_path = "test_image_output/t1.jpg"
cv2.imwrite(output_path, img)



img = cv2.imread("test_image/test2.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


objects = cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=20,
    minSize=(500, 500)
)

for (x, y, w, h) in objects:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


output_path = "test_image_output/t2.jpg"
cv2.imwrite(output_path, img)





img = cv2.imread("test_image/test3.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


objects = cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(400, 400)
)

for (x, y, w, h) in objects:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


output_path = "test_image_output/t3.jpg"
cv2.imwrite(output_path, img)

