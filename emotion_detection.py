import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = my_obj, headers = header)

    formatted_response = json.loads(response.text)
    
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    dictionary = {anger_score: 'anger', disgust_score: 'disgust',
        fear_score: 'fear', joy_score: 'joy', sadness_score: 'sadness'}
    dominant_emotion = dictionary.get(max(dictionary))
    
    return {'anger': anger_score, 'disgust': disgust_score,
        'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score,
        'dominant_emotion': dominant_emotion}