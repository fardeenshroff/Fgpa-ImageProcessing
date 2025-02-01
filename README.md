
FPGA-Based Image Processing

Enhancing Digital Images Using Hardware Acceleration

Author: Fardeen Shroff
Date: January 30, 2025
Repository Link: GitHub Repo


---

Project Overview

This project implements real-time image processing on FPGA using Verilog/VHDL, enabling edge detection, noise reduction, and contrast adjustment. The system integrates OpenCV-based software validation to compare software and hardware performance.


---

Table of Contents

1. Introduction


2. Objectives


3. FPGA Design


4. Software Validation (OpenCV)


5. Testing & Results


6. Analysis & Performance Evaluation


7. Future Improvements


8. Setup & Installation


9. Contributing


10. License




---

Introduction

Modern image processing applications require high-speed performance, which traditional CPUs struggle to provide. This project leverages FPGA parallel processing to enhance digital images in real-time.

Key Technologies Used:

FPGA Development: Verilog/VHDL

Hardware Synthesis: Xilinx Vivado / Intel Quartus Prime

Software Validation: Python + OpenCV

Algorithms Implemented: Edge Detection, Noise Filtering, Histogram Equalization



---

Objectives

Develop FPGA Modules for:

Edge Detection

Noise Reduction

Histogram Equalization


Implement Communication Interfaces:

UART

HDMI


Validate Hardware Performance using OpenCV for software comparison.



---

FPGA Design

Directory: rtl/src/

Modules Implemented:

Edge Detection: edge_detection.vhd

Noise Reduction: gaussian_filter.vhd

Histogram Equalization: histogram_equal.vhd

Top-Level Integration: top_module.vhd


Design Tools:

Synthesis & Simulation: Xilinx Vivado / Intel Quartus Prime

Target FPGA: [Specify your FPGA model here]



---

Software Validation (OpenCV)

Directory: python/

Script: opencv_validation.py

Purpose: Process identical images using OpenCV to validate and compare against FPGA results.

Key Functions:

Edge Detection: Sobel Operator

Noise Reduction: Gaussian Blur

Histogram Equalization: Contrast Adjustment



---

Testing & Results

Test Images: Located in test_images/

Results:

FPGA Processed Images: results/fpga/

OpenCV Processed Images: results/opencv/


Performance Metrics:

Processing Time: FPGA vs. OpenCV

Resource Utilization: LUTs, FFs, BRAMs

Image Quality Assessment: PSNR, SSIM



---

Analysis & Performance Evaluation

Speed: FPGA processing achieved [X]% faster performance compared to OpenCV.

Resource Efficiency: Utilized [Y]% of available FPGA resources.

Accuracy: High correlation between FPGA and OpenCV outputs with minimal discrepancies.



---

Future Improvements

Implement Additional Filters: Median, Laplacian, etc.

Optimize Resource Usage: Explore pipelining and parallelism.

Enhance Communication Interfaces: Integrate Ethernet or USB for faster data transfer.



---

Setup & Installation

1. Clone the Repository:

git clone https://github.com/fardeenshroff/fpga-imageprocessing.git
cd fpga-imageprocessing


2. FPGA Implementation:

Open the project in Xilinx Vivado or Intel Quartus Prime.

Synthesize and implement the design.

Program the FPGA with the generated bitstream.



3. Software Validation:

Ensure Python 3.x is installed.

Install OpenCV:

pip install opencv-python

Run the validation script:

python python/opencv_validation.py





---

Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.


---

License

This project is licensed under the MIT License. See the LICENSE file for details.


---

Note: Replace placeholders like [Specify your FPGA model here] with actual details from your project.

---

