# Image Text Extractor (OCR)

## Description

A simple Python tool that extracts text from images using **OpenCV preprocessing** and **Tesseract OCR**.
The script improves OCR accuracy by applying image processing steps such as resizing, thresholding, noise removal, and morphological cleaning before running Tesseract.

## Technologies

* Python
* OpenCV
* Tesseract OCR
* pytesseract
* NumPy

## Features

* Extract text from images
* Image preprocessing pipeline for better OCR accuracy
* Noise reduction and adaptive thresholding
* Lightweight single-script implementation

## Usage

1. Place your image inside the project folder.

2. Update the image path in the script:

```
image_path = "image.png"
```

3. Run the script:

```
python main.py
```

The extracted text will be printed in the terminal.

## Limitations

* OCR accuracy depends on image quality.
* Very noisy or low-resolution images may produce incorrect text.
* Complex layouts (tables or multi-column text) may require additional processing.
* Handwritten text may not be recognized accurately.

## Installation (Linux)

### 1. Clone the repository

```
git clone https://github.com/realHarshCodes/python-image-ocr.git
cd python-image-ocr
```

### 2. Create a virtual environment
```
python3 -m venv venv
```
### 3. Activate the virtual environment

```
source venv/bin/activate
```

### 4. Install Python dependencies

```
pip install opencv-python pytesseract numpy
```

### 5. Install Tesseract OCR

Ubuntu / Debian:
```
sudo apt install tesseract-ocr
```
Fedora:
```
sudo dnf install tesseract
```
### 6. Run the program
```
Image_to_String.py
```
