import cv2
import pytesseract
import numpy as np
import re
import os
import sys
import shutil
# Fedora: Tesseract is in system path, no need for explicit path
# pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

# =========================
# Preprocessing functions
# =========================

def resize_image(img, scale=2):
    """Resize image using cubic interpolation for better OCR."""
    return cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

def get_grayscale(img):
    """Convert image to grayscale."""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def remove_noise(img):
    """Remove noise using median blur."""
    return cv2.medianBlur(img, 3)

def adaptive_thresh(img):
    """Apply adaptive Gaussian thresholding."""
    return cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2
    )

def opening(img):
    """Apply morphological opening to clean image."""
    kernel = np.ones((2, 2), np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

def preprocess(img):
    """Run full preprocessing pipeline."""
    img = resize_image(img, scale=2)
    gray = get_grayscale(img)
    thresh = adaptive_thresh(gray)
    denoised = remove_noise(thresh)
    clean = opening(denoised)
    return clean

# =========================
# OCR function
# =========================

def ocr_image(img):
    """Perform OCR on preprocessed image."""
    processed = preprocess(img)
    custom_config = r'--oem 3 --psm 6'  # LSTM engine, assume block of text
    text = pytesseract.image_to_string(processed, config=custom_config)
    return text

# =========================
# Clean OCR output
# =========================

def clean_text(text):
    """Fix common OCR mistakes and remove extra whitespace."""
    text = text.replace('O ', 'C ')  # example correction
    text = re.sub(r'\s([A-D])\s', r' \1 ', text)
    text = text.replace('\n\n', '\n')
    return text.strip()

# =========================
# Main script
# =========================

if __name__ == "__main__":
    # Update this path to the image you want to process
    image_path = "image.png"
    
    if not os.path.isfile(image_path):
        print(f"Image not found at {image_path}")
        exit(1)

    # Read image
    img = cv2.imread(image_path)

    if img is None:
        print("Failed to load image. Check file path or format.")
        exit(1)

    # Perform OCR
    raw_text = ocr_image(img)
    final_text = clean_text(raw_text)

    print("----- OCR RESULT -----")
    print(final_text)


print("Python Execute with : " , sys.executable)

tesseract_path = shutil.which("tesseract")
print("Tesseract binary being used:", tesseract_path)