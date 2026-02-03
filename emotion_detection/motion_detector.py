# motion detector.py
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


def emotion_detector(text_to_analyse):
    """
    Analyzes the text for emotions and returns a structured dictionary
    containing the score for each emotion and the dominant one.

    Args:
        text_to_analyse (str): The input text to be analyzed.

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion,
              or None values if the input is invalid (Status 400).
    """

    # Retrieve API credentials from environment variables
    url = os.getenv('WATSON_URL')
    api_key = os.getenv('WATSON_API_KEY')

    # Basic validation to ensure configuration exists
    if not url:
        return {"error": "Configuration missing: WATSON_URL not found."}

    # 1. Construct the Request Payload
    # Formatting the input text into the JSON structure required by IBM Watson
    myobj = {"raw_document": {"text": text_to_analyse}}

    # 2. Set the Headers
    # Specifying the model ID for the Emotion Aggregated Workflow
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # 3. Send the POST Request
    response = requests.post(url, json=myobj, headers=header)

    # 4. Parsing Logic
    # Convert the raw response text into a Python dictionary
    formatted_response = json.loads(response.text)

    # Handling the successful response (200 OK)
    if response.status_code == 200:
        # Extracting emotions from the complex JSON structure
        # Navigation path: emotionPredictions -> [0] -> emotion
        emotion_data = formatted_response['emotionPredictions'][0]['emotion']

        # Extracting individual emotion scores
        anger_score = emotion_data['anger']
        disgust_score = emotion_data['disgust']
        fear_score = emotion_data['fear']
        joy_score = emotion_data['joy']
        sadness_score = emotion_data['sadness']

        # Aggregating scores in a temporary dictionary to calculate the maximum
        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        # Calculating the Dominant Emotion
        # Finding the key with the maximum value using a pythonic approach
        dominant_emotion = max(emotions, key=emotions.get)

        # Constructing the final output dictionary
        result = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

    # Handling Client Errors (400 Bad Request)
    # This usually occurs if the input text is empty or invalid
    elif response.status_code == 400:
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    else:
        # Handling other server errors (e.g., 500, 401, etc.)
        return {"error": f"API Error: {response.status_code}"}

    return result