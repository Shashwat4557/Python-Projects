# import required package
import cv2

# Load the B&amp;W image
img = cv2.imread('C:/Users/LENOVO/OneDrive/Desktop/vs_coding/Python/bw_image.jpg', 0)

# Check if the image has been loaded successfully
if img is None:
    print("Error: Image not loaded.")
    exit()

# Apply a pseudocolor effect to the B&amp;W image
colorized = cv2.applyColorMap(img, cv2.COLORMAP_JET)

# Save the colorized image
cv2.imwrite('colorized_image.jpg', colorized)