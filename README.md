# Stop-sign-detection-for-Rover


## Project Description 

This project implements a simple computer vision algorithm to detect STOP traffic signs using color-based detection with OpenCV in Python.
The program processes each image in the dataset, identifies red regions corresponding to stop signs, draws a bounding box, and prints the center pixel coordinates of the detected sign.
This project was developed as part of an assignment on image processing for Rover(autonomous robot).


## Requirements 

dependencies such as openCV-python


## How to Run 

Place your dataset images inside a folder named stop_sign_dataset/.

Run the program.

The program will:
    
    Convert each image into HSV color space.
    
    Apply two HSV threshold ranges (RED_LOW1–RED_HIGH1 and RED_LOW2–RED_HIGH2) to detect red regions.
    
    Filter out small contours (area < 800).
    
    Select the largest red contour as the stop sign candidate.
    
    Draw a green bounding box around it and mark the center point with a black circle.
    
    Print the center coordinates to the terminal.
    
    Save the processed images into the outputs/ folder.


## Repository Structure 
.
├── stop_sign.py          # Main detection script
├── stop_sign_dataset/    # Input dataset (place images here)
├── outputs/              # Output results (detected images are saved here)
│   ├── result_0.jpg
│   ├── result_1.jpg
│   └── ...
└── README.md             # Documentation

## HSV Thresholds for Red Detection 

The red color is split into two ranges in HSV color space:

    Range 1 → RED_LOW1 = (0, 90, 90) to RED_HIGH1 = (10, 255, 255)
    
    Range 2 → RED_LOW2 = (160, 70, 70) to RED_HIGH2 = (180, 255, 255)

These values define the lower and upper bounds of HSV ranges that cover the red hue spectrum. By combining both ranges, the stop sign can be detected reliably even when the hue wraps around the HSV circle.


## Notes & Limitations

The algorithm is purely color-based.

It may falsely detect other red objects (cars, clothes, cones).

Performance can vary under different lighting (shadows, night, glare).

For real-world autonomous driving, additional methods like shape detection or deep learning models (YOLO, Faster R-CNN) would be required.
