import cv2
import numpy as np
from util import get_limits

colors = {
    'yellow': [0, 255, 255],
    'blue': [255, 0, 0],
    'green': [0, 255, 0],
    'red': [0, 0, 255],
    'orange': [0, 165, 255]
}

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Cannot access webcam")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, bgr_color in colors.items():

        # Get HSV colour ranges
        limits = get_limits(bgr_color)

        # Create an empty mask
        mask = np.zeros(hsvImage.shape[:2], dtype=np.uint8)

        # Combine masks for every HSV range
        for lowerLimit, upperLimit in limits:
            color_mask = cv2.inRange(
                hsvImage, lowerLimit, upperLimit
            )
            mask = cv2.bitwise_or(mask, color_mask)

        # Find coloured objects
        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        for contour in contours:
            if cv2.contourArea(contour) < 500:
                continue

            x, y, w, h = cv2.boundingRect(contour)

            # Draw bounding box
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                bgr_color,
                2
            )

            # Label detected colour
            cv2.putText(
                frame,
                color_name,
                (x, max(y - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                bgr_color,
                2
            )

    cv2.imshow('Multi-Color Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()