import streamlit as st
import torch
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
from PIL import Image
from gtts import gTTS
import os

# Function to describe the image
def describe_image(image):
    # Load the pre-trained model and tokenizer
    model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    feature_extractor = ViTFeatureExtractor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

    # Preprocess the image
    if image.mode != "RGB":
        image = image.convert(mode="RGB")
    pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values

    # Generate the caption
    with torch.no_grad():
        output_ids = model.generate(pixel_values, max_length=16, num_beams=4, return_dict_in_generate=True).sequences
    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return caption

# Function to convert text to speech
def text_to_speech(text, output_audio_path):
    tts = gTTS(text=text, lang='en')
    tts.save(output_audio_path)

# Streamlit app
st.title("Image Captioning and Text-to-Speech")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:
    # Ensure the temp directory exists
    temp_dir = "./temp"
    os.makedirs(temp_dir, exist_ok=True)

    # Save the uploaded file
    image_path = f"./temp/{uploaded_file.name}"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Generate text description
    description = describe_image(image)
    st.write("Description:", description)


#if uploaded_file is not None:
    # Display the uploaded image
 #   image = Image.open(uploaded_file)
 #   st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Generate description
 #   description = describe_image(image)
 #   st.write("Description:", description)

    # Convert description to speech
    # output_audio_path = "output_audio.mp3"
    # text_to_speech(description, output_audio_path)

    # Play the audio
    #audio_file = open(output_audio_path, "rb")
    #audio_bytes = audio_file.read()
    #st.audio(audio_bytes, format="audio/mp3")
