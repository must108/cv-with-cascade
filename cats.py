import cv2

imageFile = input('Enter image file name (see assets/ for images to use!): ')
filename = 'assets/' + imageFile

image = cv2.imread(filename)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

detector = cv2.CascadeClassifier(
    'data/haarcascade_frontalcatface_extended.xml')
rects = detector.detectMultiScale(rgb, scaleFactor=1.3, 
                                  minNeighbors= 1, minSize=(75, 75))

for (i, (x, y, w, h)) in enumerate(rects):
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, "Cat Face #{}".format(i + 1), (x, y - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)

cv2.namedWindow('Cat Faces', cv2.WINDOW_NORMAL)
cv2.imshow('Cat Faces', image)
cv2.waitKey(0)