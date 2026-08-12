# 🔠 Python Image OCR

A lightweight Python OCR pipeline that extracts text from images with significantly better accuracy than raw Tesseract, thanks to a targeted **OpenCV preprocessing pipeline** — resizing, adaptive thresholding, denoising, and morphological cleaning — applied before recognition.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Image%20Processing-5C3EE8?logo=opencv&logoColor=white)
![Tesseract](https://img.shields.io/badge/Tesseract-OCR-4285F4)
![License](https://img.shields.io/badge/License-Add--LICENSE-lightgrey)

---

## 📖 Overview

Raw images — especially photos or scans with uneven lighting, low resolution, or noise — often produce poor results when passed directly to an OCR engine. This project closes that gap with a dedicated preprocessing pipeline that cleans the image *before* Tesseract ever sees it, followed by a light postprocessing pass to tidy up the extracted text.

It's a single-script, no-frills utility: point it at an image, run it, and read the result in your terminal.

---

## ⚙️ Pipeline

```
Input Image
    │
    ▼
Resize (2x, Cubic Interpolation)   → enlarges small text for the LSTM engine
    │
    ▼
Grayscale Conversion               → strips color, keeps intensity
    │
    ▼
Adaptive Gaussian Thresholding     → binarizes despite uneven lighting/shadows
    │
    ▼
Median Blur (Denoising)            → removes salt-and-pepper noise
    │
    ▼
Morphological Opening              → clears stray speckle pixels
    │
    ▼
Tesseract OCR (--oem 3 --psm 6)    → LSTM engine, assumes a block of text
    │
    ▼
Text Cleanup                       → fixes common misreads, trims whitespace
    │
    ▼
Final Extracted Text
```

Each step exists to counter a specific failure mode:

| Step | Purpose |
|---|---|
| **Resize (2x, `INTER_CUBIC`)** | Upsamples the image so character strokes are large enough for reliable recognition |
| **Grayscale conversion** | Removes irrelevant color information, simplifying the image to one channel |
| **Adaptive Gaussian threshold** | Binarizes using a *locally* computed threshold — handles shadows and uneven lighting far better than a single global threshold |
| **Median blur** | Removes salt-and-pepper noise without over-blurring text edges |
| **Morphological opening** | Erosion + dilation to clear small stray pixels/speckle noise |
| **Tesseract (LSTM, PSM 6)** | Runs OCR assuming a single uniform block of text |
| **Text cleanup** | Light regex/string fixes for common misreads and blank-line collapsing |

---

## ✨ Features

- 🖼️ Extracts text from images using Tesseract OCR
- 🧹 Full OpenCV preprocessing pipeline for real-world image accuracy
- 💡 Adaptive thresholding handles uneven lighting and shadows
- 🔇 Noise reduction via median blur + morphological opening
- 📄 Lightweight, single-script implementation — no config files
- 🩹 Basic postprocessing to clean up common OCR artifacts

---

## 🛠️ Tech Stack

- **Python 3**
- **OpenCV** (`cv2`) — image preprocessing
- **Tesseract OCR** — text recognition engine
- **pytesseract** — Python bindings for Tesseract
- **NumPy** — array operations for morphological processing

---

## 🚀 Installation (Linux)

**1. Clone the repository**
```bash
git clone https://github.com/realHarshCodes/python-image-ocr.git
cd python-image-ocr
```

**2. Create a virtual environment**
```bash
python3 -m venv venv
```

**3. Activate the virtual environment**
```bash
source venv/bin/activate
```

**4. Install Python dependencies**
```bash
pip install opencv-python pytesseract numpy
```

**5. Install Tesseract OCR**

| OS | Command |
|---|---|
| Ubuntu / Debian | `sudo apt install tesseract-ocr` |
| Fedora | `sudo dnf install tesseract` |
| macOS (Homebrew) | `brew install tesseract` |
| Windows | Install via the [UB-Mannheim Tesseract build](https://github.com/UB-Mannheim/tesseract/wiki) and add it to your system `PATH` |

**6. Verify Tesseract is on your PATH**
```bash
tesseract --version
```
If it isn't found, either add it to your `PATH`, or point `pytesseract` directly at the binary by uncommenting and editing this line near the top of `Image_to_String.py`:
```python
# pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
```

---

## ▶️ Usage

1. Place the image you want to process in the project folder.
2. Open `Image_to_String.py` and update the `image_path` variable:
   ```python
   image_path = "image.png"
   ```
3. Run the script:
   ```bash
   python Image_to_String.py
   ```
4. The extracted text is printed to the terminal under a `----- OCR RESULT -----` header. The script also prints the active Python interpreter and the resolved Tesseract binary path — handy for debugging environment/PATH issues.

---

## 📂 Repository Structure

```
python-image-ocr/
├── Image_to_String.py   # Main OCR script — preprocessing + Tesseract + cleanup
├── image.png             # Sample input image
├── Output.png             # Sample output/result
└── README.md
```

---

## ⚠️ Limitations

- OCR accuracy still depends heavily on image quality — very blurry, low-resolution, or extremely noisy images can produce garbled output.
- Complex layouts (multi-column text, tables, dense forms) may need additional preprocessing or region-based OCR.
- Handwritten text isn't reliably recognized, since Tesseract's LSTM engine is trained primarily on printed text.
- The current text-cleanup step is intentionally minimal (a couple of common character-misread fixes) — it isn't a general spell-checker.

---

## 🗺️ Roadmap

- [ ] Add command-line arguments (`argparse`) so the image path doesn't need to be hardcoded
- [ ] Support batch processing of multiple images in a folder
- [ ] Add language selection for multilingual OCR
- [ ] Export results to `.txt` / `.json` instead of only printing to console
- [ ] Add unit tests for the preprocessing functions

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for bug fixes, new preprocessing techniques, CLI improvements, or expanded language support.

---

## 👤 Author

**Harsh** — [@realHarshCodes](https://github.com/realHarshCodes)
