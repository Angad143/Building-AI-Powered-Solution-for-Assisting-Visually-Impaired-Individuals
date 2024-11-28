import streamlit as st
from PIL import Image
import os
from utils.scene_understanding import generate_scene_description
from utils.text_to_speech import text_to_speech
from utils.object_detection import detect_objects
from utils.personalized_assistance import provide_personalized_assistance
from utils.ocr_processing import extract_text_from_image
import io

# Title of the project
st.markdown(
    """
    <h1 style="background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); -webkit-background-clip: text; color: transparent;">
        AI-Powered Assistance for Visually Impaired Individuals
    </h1>
    """,
    unsafe_allow_html=True
)

# subheader of the peojects
st.subheader("This app uses Generative AI to provide these helpful features:")

st.write(
    """
       - 🌍 Real-Time Scene Understanding
       - 🗣️ Text-to-Speech Conversion
       - 🚧 Object and Obstacle Detection
       - 🤝 Personalized Assistance
    """
)

# Upload image files
uploaded_image = st.file_uploader("Please upload an image (Max 5MB) to explore the features above!", type=["jpg", "jpeg", "png"])

if uploaded_image:
    # Check if file size is within 5MB
    if uploaded_image.size <= 5 * 1024 * 1024:
        # Open the image
        image = Image.open(uploaded_image)
        
        # Save the image to the "images" folder
        save_path = os.path.join("images", uploaded_image.name)
        image.save(save_path)
        st.success(f"Image uploaded successfully!")
        
        # Display the image
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Buttons in a row for different features
        col1, col2, col3, col4 = st.columns(4)

        # Define flags to check which button was pressed
        scene_flag = False
        tts_flag = False
        obj_detect_flag = False
        assist_flag = False

        # Check button clicks and set flags
        with col1:
            if st.button("Scene Understanding"):
                scene_flag = True

        with col2:
            if st.button("Convert Text to Speech"):
                tts_flag = True

        with col3:
            if st.button("Object and Obstacle Detection"):
                obj_detect_flag = True

        with col4:
            if st.button("Personalized Assistance"):
                assist_flag = True

        # Display content based on the flags
        # Real-Time Scene Understanding
        if scene_flag:
            st.subheader("Scene Description:")

            # Read the image file as bytes (only for langchain)
            img_byte_arr = io.BytesIO() 
            image.save(img_byte_arr, format=image.format) 
            image_bytes = img_byte_arr.getvalue()

            # Generate scene description
            description = generate_scene_description(image_bytes)
            st.write(description)

        # Text-to-Speech Conversion for Visual Content
        if tts_flag:
            text = extract_text_from_image(image)
            if text.strip():
                st.subheader("Extracted Text:")
                st.write(text)

                # Path for saving audio
                output_audio_path = "audio/output_audio.mp3"

                # Convert extracted text to speech
                text_to_speech(text, output_audio_path)

                # Provide the audio for playback and download
                st.success("Text has been successfully converted to speech!")
                st.audio(output_audio_path, format="audio/mp3")
            else:
                st.warning("No text detected in the uploaded image.")

        # Object and Obstacle Detection for Safe Navigation
        if obj_detect_flag:
            st.subheader("Detected Objects:")
            detected_image = detect_objects(image)
            st.image(detected_image, caption="Objects Detected", use_container_width=True)

        # Personalized Assistance for Daily Tasks
        if assist_flag:
            st.subheader("Task-Specific Guidance:")
            guidance = provide_personalized_assistance(image)
            st.write(guidance)

    else:
        st.error("The file size exceeds the 5MB limit. Please upload a smaller image.")
