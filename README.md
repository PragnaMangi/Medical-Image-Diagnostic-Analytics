# Medical-Image-Diagnostic-Analytics

AI-powered medical image analysis using Google Gemini, Streamlit, Generative AI (GenAI), LLMs, and Multimodal AI.

> **⚠️ Disclaimer:** This project is intended for educational and research purposes only. It is **not** a substitute for professional medical advice, diagnosis, or treatment.

---

# 📖 Table of Contents

- Overview
- Features
- Technologies Used
- AI Technologies Used
- Project Architecture
- Project Structure
- Installation
- Requirements
- Getting a Gemini API Key
- Running the Application
- How It Works
- AI Output Format
- Gemini Models Used
- Future Enhancements
- Medical Disclaimer
- License
- Author

---

# 📌 Overview

Medical image analysis is an important task in healthcare that often requires expert interpretation. This application demonstrates how **Google Gemini's Multimodal AI** can assist by analyzing uploaded medical images and generating structured AI-based diagnostic reports.

Users can upload images such as:

- X-rays
- MRI Scans
- CT Scans
- Ultrasound Images
- Dental X-rays
- Skin Images
- Other medical images

The generated report includes:

- Image Type
- Findings
- Possible Diagnosis
- Confidence Level
- Recommendations
- Disclaimer

---

# ✨ Features

- 🖼️ Upload medical images (PNG, JPG, JPEG)
- 🤖 AI-powered medical image analysis
- 🧠 Uses Google Gemini Multimodal AI
- 🔄 Automatic fallback between multiple Gemini models
- 📋 Generates structured diagnostic reports
- ⚡ Fast and lightweight Streamlit interface
- 💻 Easy to run locally
- 🎯 User-friendly interface

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application Framework |
| Google Gemini API | AI Model Access |
| Google GenAI SDK | Communication with Gemini |
| Generative AI (GenAI) | AI-powered report generation |
| Large Language Model (LLM) | Medical report generation |
| Multimodal AI | Understands both images and text |
| Prompt Engineering | Structured AI responses |
| Pillow (PIL) | Image Processing |

---

# 🤖 AI Technologies Used

This project utilizes modern Artificial Intelligence technologies to analyze medical images.

### ✅ Generative AI (GenAI)

Generates detailed and structured medical analysis reports based on uploaded medical images.

### ✅ Large Language Model (LLM)

Uses Google's Gemini model to understand prompts and produce natural language medical explanations.

### ✅ Multimodal AI

Gemini processes both:

- Images
- Text prompts

allowing it to analyze medical images effectively.

### ✅ Prompt Engineering

A structured system prompt ensures consistent output in the following format:

- Image Type
- Findings
- Possible Diagnosis
- Confidence Level
- Recommendations
- Disclaimer

---

# 🏗️ Project Architecture

```
          Medical Image
                 │
                 ▼
      Streamlit File Upload
                 │
                 ▼
        Pillow (PIL Image)
                 │
                 ▼
      Prompt + Medical Image
                 │
                 ▼
      Google Gemini API
                 │
                 ▼
 Gemini Multimodal AI (LLM)
                 │
                 ▼
 AI Generated Medical Report
                 │
                 ▼
      Streamlit Interface
```

---

# 📂 Project Structure

```text
Medical-Image-Diagnostic-Analytics/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/PragnaMangi/Medical-Image-Diagnostic-Analytics.git

cd Medical-Image-Diagnostic-Analytics
```

---

## 2. Create a Virtual Environment (Optional)

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Your `requirements.txt` should contain:

```text
streamlit
google-genai
Pillow
```

---

# 🔑 Getting a Gemini API Key

1. Visit **Google AI Studio**
2. Sign in with your Google account.
3. Generate a new API Key.
4. Replace:

```python
API_KEY = "GOOGLE_API_KEY"
```

with

```python
API_KEY = "YOUR_API_KEY"
```

---

# ▶️ Running the Application

Run the application using:

```bash
streamlit run main.py
```

Then open your browser:

```
http://localhost:8501
```

---

# ⚙️ How It Works

1. Upload a medical image.
2. The image is processed using Pillow.
3. A structured medical prompt is combined with the image.
4. The request is sent to Google Gemini.
5. Gemini analyzes the image using Multimodal AI.
6. The generated report is displayed in the Streamlit interface.

---

# 📋 AI Output Format

The generated report follows this structure:

```
## Image Type

## Findings

## Possible Diagnosis

## Confidence Level

## Recommendations

## Disclaimer
```

---

# 🤖 Gemini Models Used

The application automatically attempts multiple Gemini models to improve reliability.

```python
MODELS = [
    "gemini-3.5-flash",
    "gemini-3.1-flash-image",
    "gemini-3.1-flash-image-preview",
    "gemini-3.1-flash-lite",
    "gemini-flash-latest"
]
```

---

# 🔮 Future Enhancements

- 📄 PDF Report Download
- 🩻 DICOM Image Support
- 📊 Disease Probability Charts
- 🔐 User Authentication
- ☁️ Cloud Deployment
- 🌍 Multi-language Support
- 📚 Report History
- 🧠 Explainable AI (XAI)
- 🏥 Hospital System Integration

---

# ⚠️ Medical Disclaimer

The AI-generated report is for **educational and research purposes only**.

It should **not** be used as a substitute for:

- Professional medical advice
- Diagnosis
- Treatment
- Clinical decision-making

Always consult a qualified healthcare professional for any medical concerns.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👩‍💻 Author

**Pragna Mangi**

**B.Tech – Computer Science & Engineering (AI & ML)**

**GitHub Repository:** https://github.com/PragnaMangi/Medical-Image-Diagnostic-Analytics

---


### 🚀 Built with Python, Streamlit, Google Gemini AI, Generative AI (GenAI), Large Language Models (LLMs), Multimodal AI, and Prompt Engineering.
