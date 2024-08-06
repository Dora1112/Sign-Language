from flask import Flask, render_template, request, send_file
import os
import random
import cv2
from PIL import Image
import numpy as np

app = Flask(__name__)

DISPLAY_WIDTH = 400
DISPLAY_HEIGHT = 300

def predict_word(text):
    return text

def fetch_image(word, image_dir='./static/images'):
    word_dir = os.path.join(image_dir, word)
    if not os.path.exists(word_dir):
        raise FileNotFoundError(f"No directory found for the word: {word}")

    images = [f for f in os.listdir(word_dir) if os.path.isfile(os.path.join(word_dir, f))]
    if not images:
        raise FileNotFoundError(f"No images found in directory: {word_dir}")
    
    image_path = os.path.join(word_dir, random.choice(images))
    return image_path

def fetch_video(word, video_dir='./static/videos'):
    word_dir = os.path.join(video_dir, word)
    if not os.path.exists(word_dir):
        raise FileNotFoundError(f"No directory found for the word: {word}")

    videos = [f for f in os.listdir(word_dir) if os.path.isfile(os.path.join(word_dir, f))]
    if not videos:
        raise FileNotFoundError(f"No videos found in directory: {word_dir}")

    video_path = os.path.join(word_dir, random.choice(videos))
    return video_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/word', methods=['POST'])
def predict():
    text = request.form['input_text']
    word = predict_word(text)
    response = {'status': 'ok'}
    
    try:
        image_path = fetch_image(word)
        response['image_path'] = image_path
    except FileNotFoundError as e:
        response['image_error'] = str(e)
    
    try:
        video_path = fetch_video(word)
        response['video_path'] = video_path
    except FileNotFoundError as e:
        response['video_error'] = str(e)
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
