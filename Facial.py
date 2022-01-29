# Facial Recognition System

import os
import io
import json
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import requests
from PIL import Image, ImageDraw, ImageFont

"""
Example 1. Detect faces from an image (from the web)
"""

API_KEY = 'f8274f5d05fe45798cf4e0aaf021789c'
ENDPOINT = 'https://faceapp2.cognitiveservices.azure.com/'

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))
image_url = 'https://lh3.googleusercontent.com/pw/AM-JKLWihuQfkjmAu7AG5xRaoCnB9PI5VI6dZGcXhqVtIMk6L9swLa0M8WziWt0uVOTjTEY03WKKzAppzFt62mbpYT9C5x5n-gI0S8TmfOzUOg2X6CceLspAVqWSKyXN96r7C6YNHSGXUw7xm1wK2utNAAjNXg=w2249-h1686-no?authuser=0'
image_name = os.path.basename(image_url)

response_detected_faces = face_client.face.detect_with_url(
    image_url,
    detection_model='detection_03',
    recognition_model='recognition_04'

)
print(response_detected_faces)

if not response_detected_faces:
    raise Exception('No face detected')

print('Number of people detected: {0}'.format(len(response_detected_faces)))

response_image = requests.get(image_url)
img = Image.open(io.BytesIO(response_image.content))
draw = ImageDraw.Draw(img)

for face in response_detected_faces:
    rect = face.face_rectangle
    left = rect.left
    top = rect.top
    right = rect.width + left
    bottom = rect.height + top
    draw.rectangle(((left, top), (right, bottom)), outline='green', width=5)
img.show()
img.save('test1.jpg')


"""
Example 2. Detect faces landmarks from an image (from a local file)
"""

img_file = open(r'.\Images\group.jpg', 'rb')

response_detected_faces = face_client.face.detect_with_stream(
    image=img_file,
    detection_model='detection_03',
    recognition_model='recognition_04',
    return_face_landmarks=True
)

if not response_detected_faces:
    raise Exception('No face detected')

print('Number of people detected: {0}'.format(len(response_detected_faces)))

print(vars(response_detected_faces[0]))
print(vars(response_detected_faces[0].face_landmarks).keys())
print(response_detected_faces[0].face_landmarks.mouth_left)

img =Image.open(img_file)
draw = ImageDraw.Draw(img)

for face in response_detected_faces:
    rect = face.face_rectangle
    left = rect.left
    top = rect.top
    right = rect.width + left
    bottom = rect.height + top
    draw.rectangle(((left, top), (right, bottom)), outline='green', width=5)

    # mark the noise tip
    x = face.face_landmarks.nose_tip.x
    y = face.face_landmarks.nose_tip.y
    draw.rectangle(((x, y), (x, y)), outline='white', width=7)

    # draw the bounding box around the mouth
    mouth_left = face.face_landmarks.mouth_left.x, face.face_landmarks.mouth_left.y
    mouth_right = face.face_landmarks.mouth_right.x, face.face_landmarks.mouth_right.y
    lip_bottom = face.face_landmarks.under_lip_bottom.x, face.face_landmarks.under_lip_bottom.y
    draw.rectangle((mouth_left, (mouth_right[0], lip_bottom[1])), outline='yellow', width=2)

img.show()
img.save('test2.jpg')


"""
Example 3. Guess a person's emotion & age
"""

img_file = open(r'.\Images\Pic3.jpg', 'rb')

response_detection = face_client.face.detect_with_stream(
    image=img_file,
    detection_model='detection_01',
    recognition_model='recognition_04',
    return_face_attributes=['age', 'emotion'],
)

img = Image.open(img_file)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(r'C:\Users\ashis\OneDrive\Desktop\python\AzureVision\Images\arial.ttf', 35)
for face in response_detection:
    age = face.face_attributes.age
    emotion = face.face_attributes.emotion
    neutral = '{0:.0f}%'.format(emotion.neutral * 100)
    happiness = '{0:.0f}%'.format(emotion.happiness * 100)
    anger = '{0:.0f}%'.format(emotion.anger * 100)
    sandness = '{0:.0f}%'.format(emotion.sadness * 100)

    rect = face.face_rectangle
    left = rect.left
    top = rect.top
    right = rect.width + left
    bottom = rect.height + top
    draw.rectangle(((left, top), (right, bottom)), outline='green', width=5)

    draw.text((right + 4, top), 'Age: ' + str(int(age)), fill=(255, 255, 255), font=font)
    draw.text((right + 4, top+35), 'Neutral: ' + neutral, fill=(255, 255, 255), font=font)
    draw.text((right + 4, top+70), 'Happy: ' + happiness, fill=(255, 255, 255), font=font)
    draw.text((right + 4, top+105), 'Sad: ' + sandness, fill=(255, 255, 255), font=font)
    draw.text((right + 4, top+140), 'Angry: ' + anger, fill=(255, 255, 255), font=font)

img.show()
img.save('test3.jpg')



"""
Example 4. Detect if a face shows up in other photos/images
"""


response_detected_faces = face_client.face.detect_with_stream(
    image=open(r'.\Images\Pic2.jpg', 'rb'),
    detection_model='detection_03',
    recognition_model='recognition_04',  
)
face_ids = [face.face_id for face in response_detected_faces]

img_source = open(r'.\Images\group.jpg', 'rb')
response_face_source = face_client.face.detect_with_stream(
    image=img_source,
    detection_model='detection_03',
    recognition_model='recognition_04'    
)
face_id_source = response_face_source[0].face_id

matched_faces = face_client.face.find_similar(
    face_id=face_id_source,
    face_ids=face_ids
)

img = Image.open(open(r'.\Images\Pic2.jpg', 'rb'))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(r'C:\Users\ashis\OneDrive\Desktop\python\AzureVision\Images\arial.ttf', 25)

for matched_face in matched_faces:
    for face in response_detected_faces:
        if face.face_id == matched_face.face_id:
            rect = face.face_rectangle
            left = rect.left
            top = rect.top
            right = rect.width + left
            bottom = rect.height + top
            draw.rectangle(((left, top), (right, bottom)), outline='green', width=5)
img.show()
img.save('test4.jpg')


"""
Example 5. Check if a perosn in differnet images are the same perosn
"""

face_verified = face_client.face.verify_face_to_face(
    face_id1=matched_faces[0].face_id,
    face_id2='371e00f4-b5a5-4030-8473-3388d7016423'
    
)
print(face_verified.is_identical)