import cv2
img = cv2.imread('image.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray, 1.1, 4)
print('Number of detected faces:', len(faces))

if len(faces) > 0:
    for i, (x, y, w, h) in enumerate(faces):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        face = img[y:y + h, x:x + w]
        cv2.imshow(f"Cropped Face {i}", face)
        cv2.imwrite(f'face-{i}.jpg', face)
        print(f"face{i}.jpg is saved")

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
