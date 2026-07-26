Markdown

# Multilingual Street Sign OCR & Gemini Translation Tool

A Python-based computer vision application that reads text from street signs or images using **EasyOCR** (with support for Traditional Chinese and English), visualizes the bounding boxes and extracted text on the image via **OpenCV**, and uses Google's **GenAI SDK (`gemini-3.5-flash`)** to translate the extracted text into English.

---

## Libraries Used

1. **OpenCV** (`cv2`) – For loading images, drawing bounding boxes (`cv2.rectangle`), overlaying text (`cv2.putText`), and displaying the processed image window.
2. **EasyOCR** (`easyocr`) – For Optical Character Recognition (OCR) to detect and extract text from images (configured for English and Traditional Chinese `ch_tra`).
3. **Google GenAI SDK** (`google.genai`) – For leveraging Google's Gemini models (`gemini-3.5-flash`) to perform AI-driven translation of the extracted text.

---

## Installation

Ensure you have Python installed, then install the required dependencies using pip:

```
cmd
pip install opencv-python easyocr google-genai
```

## How to Run

    API Key Setup: Make sure your Google GenAI API key is properly configured in the script (or ideally, loaded via environment variables for security).

    Image Path: Place a target image file inside a folder named StreetSigns and name it newtest.jpg (or update the imagepath variable in the script to match your file).

    Execute: Run the script from your terminal:

        ```
        DOS

        python script_name.py
        ```

## Features & Logic

    Dual Reader Pipeline: Initializes EasyOCR readers for multi-language detection (ch_tra for Traditional Chinese and en for English).

    Visual Annotation: Iterates through OCR results, draws custom-colored bounding boxes around detected text blocks directly onto the image, and overlays the recognized text.

    AI Translation: Aggregates the extracted Chinese text lines and sends them to the Gemini API (gemini-3.5-flash) to generate a clean, context-aware English translation.

    Interactive Display: Opens an OpenCV display window showing the annotated image (press any key to close the window).
