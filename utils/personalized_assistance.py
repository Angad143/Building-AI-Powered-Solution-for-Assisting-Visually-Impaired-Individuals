import google.generativeai as genai
# import cv2
# import numpy as np
# from PIL import Image

# Analyze the uploaded image and provide personalized guidance or assistance.
def provide_personalized_assistance(image):
    # Open and read API key
    f = open("keys/gemini_key.txt")
    key = f.read()

    # Configure the google api key
    genai.configure(api_key=key)

    # # Convert PIL image to NumPy for OpenCV compatibility
    # opencv_image = np.array(image)  
    # opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR)

    ## Extracting labels or text from the image using OCR (optional)
    # ocr_result = pytesseract.image_to_string(opencv_image)
    # prompt_context = f"The image contains the following text: {ocr_result}"

    # Initialize a Generative AI model with the provided model name and API key
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    # Generate a task-specific prompt
    prompt = (
        "Analyze the uploaded image and provide personalized suggestions."
        "Describe objects, labels, or context that can assist the user in daily tasks."
    )

    # Generate response using the Generative AI API
    try:
         # Call the Generative AI API to generate the content
        response = model.generate_content([image, prompt])
        if response:
            return response.text  
        else:
            return "Unable to provide personalized guidance."
        
    except Exception as e:
        return f"Error occurred while processing the image: {e}"

