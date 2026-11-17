import numpy as np
import cv2


def get_limits(color):
    c = np.uint8([[color]])  # BGR colour values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = int(hsvC[0, 0, 0])

    lower_hue = hue - 10
    upper_hue = hue + 10

    def make_range(low, high):
        lower = np.array([low, 100, 100], dtype=np.uint8)
        upper = np.array([high, 255, 255], dtype=np.uint8)
        return lower, upper

    # Handle colours wrapping around the lower HSV boundary
    if lower_hue < 0:
        return [
            make_range(0, upper_hue),
            make_range(180 + lower_hue, 179)
        ]

    # Handle colours wrapping around the upper HSV boundary
    if upper_hue > 179:
        return [
            make_range(lower_hue, 179),
            make_range(0, upper_hue - 180)
        ]

    return [make_range(lower_hue, upper_hue)]