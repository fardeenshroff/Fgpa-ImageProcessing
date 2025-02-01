# FPGA-ImageProcessing Project

This project involves implementing various image processing techniques on FPGA and validating them using Python and OpenCV. Below are the details of the **OpenCV Testing** module that you can use to test the edge detection functionality.

## OpenCV Testing: Edge Detection

The following Python script demonstrates the use of **OpenCV's Canny Edge Detection** algorithm to detect edges in an image.

### Code: `opencv_edge_detection.py`

```python
import numpy as np
import cv2

def test_edge_detection():
    # Example function to test edge detection using OpenCV
    image = np.zeros((100, 100), dtype=np.uint8)
    edges = cv2.Canny(image, 100, 200)
    print("Edge detection output:", edges)

if __name__ == "__main__":
    test_edge_detection()
    print("Script is running!")