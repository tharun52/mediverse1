import cv2
import numpy as np

def preprocess(img):
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply binarization and inversion
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    return binary

def segment_words(img):
    # Find contours
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    word_images = []
    for cnt in contours:
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(cnt)
        
        # Aspect ratio and area filters to exclude non-word components
        aspect_ratio = w / float(h)
        area = w * h
        if aspect_ratio < 0.1 or aspect_ratio > 10 or area < 100 or area > 10000:
            continue
        
        # Extract the region of interest (ROI)
        roi = img[y:y+h, x:x+w]
        
        # Append the ROI to the list of word images
        word_images.append(roi)
    
    return word_images

# Load the handwritten image
image = cv2.imread(r'test06.png') #avoid raw strings, image path goes here

# Preprocess the image
preprocessed = preprocess(image)

# Segment the words
word_images = segment_words(preprocessed)

# Display the word images
for i, word in enumerate(word_images):
    cv2.imshow(f'Word {i+1}', word)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
