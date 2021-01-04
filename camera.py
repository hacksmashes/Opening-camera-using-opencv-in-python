import cv2

cam=cv2.VideoCapture(0)
print("opening camera...")
print("press esc button to turn off the camera")
while True:
    img=cam.read()[1]
    cv2.imshow("Cam feed",img)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break    
cam.release()
cv2.destroyAllWindows()


