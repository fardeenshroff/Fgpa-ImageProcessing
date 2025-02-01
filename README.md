# FPGA-ImageProcessing

This project involves implementing various image processing techniques on FPGA and validating them using Python and OpenCV. Below are the details of the OpenCV Testing module that you can use to test the edge detection functionality.

## Project Structure

📂 FPGA-ImageProcessing │── 📂 fpga_design/        # Verilog/VHDL Image Processing Modules │── 📂 opencv_testing/     # Python + OpenCV for Software Reference │── 📂 reports/            # Performance Comparison & Research │── README.md              # Project Overview │── LICENSE                # Open-Source License

## OpenCV Testing: Edge Detection

The following Python script demonstrates the use of OpenCV's Canny Edge Detection algorithm to detect edges in an image.

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

How to Run:

1. Clone this repository to your local machine.


2. Install required dependencies:

pip install numpy opencv-python


3. Run the script:

python opencv_edge_detection.py



License

This project is licensed under the MIT License - see the LICENSE file for details.

Future Works

Optimization of image processing algorithms.

Exploration of additional image processing techniques.
