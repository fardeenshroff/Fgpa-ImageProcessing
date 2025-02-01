# FPGA-ImageProcessing Project

This project involves implementing various image processing techniques on FPGA (Field-Programmable Gate Array) and validating the results using Python and OpenCV. The primary goal is to compare the hardware-based FPGA implementation with a software-based reference using OpenCV.

## Table of Contents

- [Project Overview](#project-overview)
- [Implemented FPGA Modules](#implemented-fpga-modules)
- [OpenCV Testing: Edge Detection](#opencv-testing-edge-detection)
- [How to Run](#how-to-run)
- [License](#license)
- [Future Work](#future-work)
- [Contributing](#contributing)

## Project Overview

This repository contains various modules and files related to implementing image processing algorithms on FPGA. It also includes validation scripts using Python and OpenCV for comparison. The project includes image processing modules such as edge detection, noise reduction, histogram equalization, and image transmission over different protocols like UART and HDMI.

## Implemented FPGA Modules

The following FPGA modules have been implemented in Verilog/VHDL for image processing:

- **Edge Detection (Using Canny Filter)** – `edge_detection.vhd`
- **Noise Reduction (Gaussian Filter)** – `gaussian_filter.vhd`
- **Histogram Equalization** – `histogram_equal.vhd`
- **Image Transmission (UART/HDMI)** – `uart_interface.vhd`, `hdmi_display.vhd`

## OpenCV Testing: Edge Detection

The following Python script demonstrates the use of **OpenCV's Canny Edge Detection** algorithm to detect edges in an image. This serves as a software-based reference to validate the results from the FPGA implementation.

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

Description:

This script creates a 100x100 black image using NumPy.

It applies Canny Edge Detection to the image using OpenCV's cv2.Canny() function.

The detected edges are printed to the console, providing a visual representation of the result.


How to Run:

1. Install Python 3.x and dependencies:

pip install opencv-python


2. Save the code in a Python file, for example opencv_edge_detection.py.


3. Run the script:

python opencv_edge_detection.py



Output:

You will see the detected edges printed in the terminal, representing the result of the edge detection applied on the black image.

How to Run

Follow these steps to run the project:

1. Clone the repository:

git clone https://github.com/fardeenshroff/fpga-imageprocessing.git


2. Navigate to the project directory:

cd fpga-imageprocessing


3. Install the necessary dependencies:

pip install -r requirements.txt


4. For FPGA-related design files, ensure you have a compatible FPGA development environment set up. Refer to the documentation for further FPGA-specific setup instructions.


5. To run the OpenCV-based validation script, use:

python opencv_edge_detection.py



License

This project is licensed under the MIT License.

Future Work

In the future, the project will expand to include:

More FPGA image processing algorithms like Convolution, Edge Detection (Sobel), etc.

Advanced validation tools using Python for automated comparisons of FPGA and software results.

Optimizing FPGA implementations for higher performance and lower resource utilization.

Integration with hardware devices like cameras for real-time processing and visualization.


Contributing

Contributions are welcome! To contribute:

1. Fork the repository.


2. Create a new branch (git checkout -b feature-name).


3. Make your changes and commit them (git commit -m 'Add feature').


4. Push to the branch (git push origin feature-name).


5. Open a pull request.



Please make sure to update tests as appropriate and follow the coding style of the repository.

Acknowledgments

Thanks to the OpenCV documentation for providing the necessary resources for image processing.

Special thanks to the FPGA community for their continuous contributions to hardware design and processing.


