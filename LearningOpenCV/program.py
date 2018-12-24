import cv2
print(cv2.__version__)

image = cv2.imread(".\\LearningOpenCV\Surface Laptop 2.jpg", 0)
cv2.imshow("image test", image)
cv2.waitKey()
cv2.destroyWindow("image test")

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()