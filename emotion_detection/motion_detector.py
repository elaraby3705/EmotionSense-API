# motion_detector.py
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


def emotion_detector(text_to_analyse):
    """
    Function to send text to the IBM Watson NLP library for emotion analysis.

    Args:
        text_to_analyse (str): The text input to be analyzed.

    Returns:
        str: The raw response text from the API.
    """

    # 1. Retrieve the Service URL from environment variables
    url = os.getenv('WATSON_URL')

    # Validation step to ensure URL exists
    if not url:
        return "Error: WATSON_URL is missing in .env file."

    # 2. Construct the Request Payload
    # IBM Watson requires the text to be wrapped in a specific JSON structure
    myobj = {"raw_document": {"text": text_to_analyse}}

    # 3. Set the Headers
    # This specific header tells the API which model to use (Emotion Aggregated Workflow)
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # 4. Send the POST Request
    # We send the URL, the JSON object, and the required headers
    response = requests.post(url, json=myobj, headers=header)

    # 5. Return the Response
    # For Milestone 2, we return the raw text to verify the connection
    return response.text