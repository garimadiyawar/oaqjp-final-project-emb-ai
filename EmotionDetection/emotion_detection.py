import json 
import requests

def emotion_detector(text_to_analyze):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    header={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    formatted_response = json.loads(response.text)

    try:
        emotion_values = formatted_response['emotionPredictions'][0]['emotion']
    except (KeyError, IndexError):
        # Return None values if there is an issue with the response structure
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
        
    anger_score= emotion_values['anger']
    disgust_score= emotion_values['disgust']
    fear_score= emotion_values['fear']
    joy_score= emotion_values['joy']
    sadness_score= emotion_values['sadness']
    dominant_emotion = max(emotion_values, key=emotion_values.get)

    
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }