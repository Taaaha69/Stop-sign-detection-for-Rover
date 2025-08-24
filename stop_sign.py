import cv2
import glob
import os

# macros
RED_LOW1 = (0, 90, 90)
RED_HIGH1 = (10, 255, 255)
RED_LOW2 = (160, 70, 70)
RED_HIGH2 = (180, 255, 255)


# Ensure output directory exists
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True) # Creates an output directory if file doesn't exist

# Load dataset images
image_paths = glob.glob("stop_sign_dataset/*.jpg")
if not image_paths:
    print("Error: No .jpg files found in stop_sign_dataset/")
    exit(1)


# Process each image
for i, path in enumerate(image_paths):
    image = cv2.imread(path)
    if image is None:
        print(f"Error: Could not load {path}")
        continue

    # Detect red regions

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)   # Convert to HSV

    # Get mask
    mask1 = cv2.inRange(hsv, RED_LOW1, RED_HIGH1)
    mask2 = cv2.inRange(hsv, RED_LOW2, RED_HIGH2)
    red_mask = cv2.bitwise_or(mask1, mask2)

    # Applying blur
    red_mask = cv2.GaussianBlur(red_mask, (5, 5), 0)

    # Find contours
    contours, trash = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    candidates = [c for c in contours if cv2.contourArea(c) > 800]

    stop_sign_contour= max(candidates, key=cv2.contourArea)

    if stop_sign_contour is not None:
        x, y, w, h = cv2.boundingRect(stop_sign_contour)
        cx, cy = x + w // 2, y + h // 2

        # Draw rectangle + center
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.circle(image, (cx, cy), 7, (0, 0, 0), -1)

        print(f"{path}. Center: ({cx}, {cy})")
    else:
        print(f"{path}. No stop sign detected")

    # Save output
    output_path = os.path.join(output_dir, f"result_{i}.jpg")
    cv2.imwrite(output_path, image)

print("Processing completed, results saved in /outputs ")