import cv2
import mediapipe as mp
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Get the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Cannot open webcam. Make sure you have permission to access the webcam.")
    exit()

while True:
    # Read a frame from the webcam
    ret, image = cap.read()

    # Check if the frame is read correctly
    if not ret:
        print("Cannot read a frame from webcam. Try again.")
        break

    # Display the frame
    cv2.imshow('Webcam', image)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()