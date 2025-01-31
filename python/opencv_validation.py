import numpy as np
import cv2

def test_edge_detection():
    # Example function to test edge detection using OpenCV
    image = np.zeros((100, 100), dtype=np.uint8)
    edges = cv2.Canny(image, 100, 200)
    print("Edge detection output:", edges)

if __name__ == "_main_":
    test_edge_detection()
    print("script is running!")