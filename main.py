import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

cv2.namedWindow("video")

video_path = "balling.mp4"
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)

l_roi = np.array([0, 100, 100])
u_roi = np.array([30, 255, 255])
l_blue = np.array([90, 50, 50])
u_blue = np.array([130, 255, 255])

kernel = np.ones((5, 5), np.uint8)
is_collided = False
collisions = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    m_roi = cv2.inRange(hsv, l_roi, u_roi)
    m_blue = cv2.inRange(hsv, l_blue, u_blue)
    m_blue = cv2.dilate(m_blue, kernel, iterations=3)
    roi_and_blue = cv2.bitwise_and(m_blue, m_roi)

    is_colliding = np.any(roi_and_blue > 0)
    if not is_collided and is_colliding:
        collisions += 1
        print("collisions: {}".format(collisions))
    collided = colliding

    cv2.imshow("video", frame)
    key = cv2.waitKey(int(fps)) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
