import streamlit as st
from google import genai
from PIL import Image
import time

# ===============================
# Configure Gemini API
# ===============================
API_KEY = "GOOGLE_API_KEY"  

client = genai.Client(api_key=API_KEY)

# ===============================
# Streamlit Page
# ===============================
st.set_page_config(
    page_title="Medical Image Analysis",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Medical Image Diagnostic Analytics")

st.write(
    """
Upload a medical image (X-Ray, MRI, CT Scan, Ultrasound, etc.)
and Gemini AI will analyze it.
"""
)

# ===============================
# Prompt
# ===============================
system_prompt = """
You are an expert medical AI assistant.

Analyze the uploaded medical image carefully.

Return your answer in this format:

## Image Type

## Findings

## Possible Diagnosis

## Confidence Level

## Recommendations

## Disclaimer

Mention that this is AI-generated and should not replace a doctor's diagnosis.
"""

# ===============================
# Upload
# ===============================
uploaded_file = st.file_uploader(
    "Upload Medical Image",
    type=["png", "jpg", "jpeg"]
)

# ===============================
# Available models (best → fallback)
# ===============================
MODELS = [
    "gemini-3.5-flash",
    "gemini-3.1-flash-image",
    "gemini-3.1-flash-image-preview",
    "gemini-3.1-flash-lite",
    "gemini-flash-latest",
]

# ===============================
# Button
# ===============================
if st.button("Generate Image Analysis"):

    if uploaded_file is None:
        st.warning("Please upload an image.")
        st.stop()

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    success = False

    for model_name in MODELS:

        try:

            with st.spinner(f"Trying {model_name}..."):

                response = client.models.generate_content(
                    model=model_name,
                    contents=[
                        system_prompt,
                        image
                    ]
                )

            st.success(f"Analysis completed using {model_name}")

            st.subheader("Medical Analysis Report")

            st.markdown(response.text)

            success = True

            break

        except Exception:

            time.sleep(2)

    if not success:
        st.error(
            "None of the available Gemini models responded successfully. "
            "Please try again after a few minutes."
        )
