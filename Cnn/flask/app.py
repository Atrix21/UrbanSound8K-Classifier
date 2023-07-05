from flask import Flask,request,jsonify
import tensorflow as tf
import librosa
import numpy as np

app = Flask(__name__)

model = tf.keras.models.load_model('weights.best.basic_cnn.hdf5')

d = {0: 'air_conditioner', 1: 'car_horn', 2: 'children_playing', 3: 'dog_bark', 4: 'drilling', 5: 'engine_idling', 6:'gun_shot', 7: 'jackhammer', 8: 'siren', 9: 'street_music'}

def func(filename):
    max_pad_len = 215
    audio, sample_rate = librosa.load(filename) 
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    pad_width = max_pad_len - mfccs.shape[1]
    feat = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')
    feat = feat.reshape(40, 1, 1)
    batch_size=1 # example batch size
    feat = np.reshape(feat, (batch_size,) + feat.shape)
    pred = str(np.argmax(model.predict(feat)))
    return class_map[pred]

@app.route('/predict',methods=['POST'])
def predict():
    if 'audio' not in request.files:
        return 'No file provided', 400

    audio_file = request.files['audio']
    if not audio_file.filename.lower().endswith('.wav'):
        return 'Invalid file type, must be .wav', 400
    preditction = func(audio_file)
    print(preditction)
    return preditction

if __name__ == '__main__':
    app.run(debug=True)
